import random
import libnum
import hashlib
import argparse
import time
import sys
import logging as log
from web3 import Web3

from Web3_util import  get_contract_values, mod_hash_eth

from Pietrzak_VDF import VDF, gen_recursive_halving_proof, verify_recursive_halving_proof, get_exp


### Unitility functions


    
def hash(*strings): # utility function for string hash
    r = hashlib.sha3_256()
    input = ''.join(map(str, strings))
    r.update(input.encode('utf-8'))
    
    return r.hexdigest()
    
def power(a,b,m):   # a^b mod m
    result = 1
    while b > 0:
        if b % 2 != 0:
            result = (result * a) % m
        b //= 2
        a = (a * a) % m

    return result
    
    
def simple_VDF(a, N, T):
    a = (a*a)%N
    for i in range(T-1):
        a = (a*a)%N
    return a
    

### Bicorn Mechanism

def GGen(N): # security parameter lambda can be omitted
    g = random.randint(2, N)
    # Let g be a quadratic residue mod N. then, we can use QR+ to satisfy the low order assumption
    g = pow(g, 2, N)
    
    return g


def construct_claim(exp_list, N, g, y, T):
    # If T is odd, make the half of T even
    if T%2 == 0:
        T_half = int(T/2)
    else:
        T_half = int((T+1)/2)   
            
    # v = get_exp(exp_list, pow(2,T_half), N)    
    v = VDF(N, g, T_half)
    
    return (N, g, y, T, v)


# Returns N=p*q where p and q are primes
def generate_divisor(bitsize):
    p=libnum.generate_prime(bitsize)
    q=libnum.generate_prime(bitsize)
    N=p*q
    print ("\nPrime*Prime (N): %d. Length: %d bits, Digits: %d" % (N,libnum.len_in_bits(N), len(str(N)) ))
    return N
 

def select_automatic_mode():
    round_info, stage, value_at_round, commits = get_contract_values()
     
    if stage == "Finished":
    
        print('There is no active round found')
        print()
        ans = input('Do you want to set up a new round? (y or n):')
        
        if ans.lower() == 'y':            
            bitsize = int(input("Input bit size (2048 is recommended): "))
            N = generate_divisor(bitsize)
            g = GGen(N)	
            T = int(input("Input time delay (Over 100000 is recommended): "))
            
            return {
                "mode": "auto-setup",
                "N": N,
                "g": g,
                "T": T,
            }
            
        elif ans.lower() == 'n':
            print('There is nothing to run. This script terminates.') 
            exit()
            
        else:
            print("Invalid selection. Please try again.")
            select_automatic_mode()
    
    elif stage == "Reveal":

        print(f'Round {round_info} is active with Stage {stage}')
        ans = input(f'Do you want to recover RANDOM for Round {round_info+1}? (y or n):')
        
        if ans.lower() == 'y':
            N = value_at_round['n']
            g = value_at_round['g']
            T = value_at_round['T']
            bstar = value_at_round['bStar']
            commits = commits
            
            return {
                "mode": "auto-recover",
                "N": N,
                "g": g,
                "T": T,
                "bstar": bstar,
                "commits": commits
            }
            
            
        elif ans.lower() == 'n':
            print('There is nothing to run. This script terminates.') 
            exit()
            
        else:
            print("Invalid selection. Please try again.")
            select_automatic_mode()
    
    else:
        print('The contract is on the Commit phase. There is nothing to run. This script terminates.')
        exit()
        
    return 
    
def select_mode():
    print("Select a mode (1 or 2):")
    print("1. Manual: A user manually inputs numbers")
    print("2. Automatic (Recommended): This program gets inputs from the smart contract on the Ethereum compatible network")
    print("3. Use the default test option (2048RSA, 10s delay)")
    choice = input("Choose: ")
    print()

    if choice == "1":
        bitsize = int(input("Input bit size (2048 is recommended): "))
        N = generate_divisor(bitsize)
        g = GGen(N)
        T = int(input("Input time delay (Over 10000000 is recommended): "))
        member = int(input("Input number of members: "))
        return {
                "mode": "Manual",
                "N": N,
                "g": g,
                "T": T,
                "member": member
            }
        
    elif choice == "2":
        return select_automatic_mode()
        
    elif choice == "3":
        N = generate_divisor(2048)
        g = GGen(N)
        T = 1000
        member = 3
        return {
                "mode": "Test",
                "N": N,
                "g": g,
                "T": T,
                "member": member
            }
        
    else:
        print("Invalid selection. Please try again.")
        select_mode()
        
        
def setup(N, g, T):

    print('\n------------------------------------------------\n')
    print('Setup Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] Setup environment:')
    print('\t - Description of QR+ Group: ', N)
    print('\t - Time Delay for VDF (T): ', T)
    print('\t - Group generator (g): ', g)
    
    # Compute h <- g^(2^t), optionally with PoE
    #h, proof = simple_VDF(g)
    start = time.time()
    h, exp_list = VDF(N, g, T, True)
    end = time.time()   
    print(f'\t - h: {h} computed in {end - start:.5f} sec')
    print('')

    # Proof-of-Exponentiation proof & verification
    claim = construct_claim(exp_list, N, g, h, T)

    start = time.time()    
    proof_list_setup = gen_recursive_halving_proof(claim)
    end = time.time()    
    print(f'[+] The PoE Proof List is generated in {end - start:.5f} sec')    
    print(f"[+] The generated VDF proof for h:")
    print(*proof_list_setup, sep='\n')    
    
    start = time.time()  
    test = verify_recursive_halving_proof(proof_list_setup)   
    end = time.time()    
    
    if (test==True):
        print(f"\n[+] Verification Success in {end - start:.5f} sec")
    else:
        print("\n[-] Verifier rejects the prover's VDF claim")    

    print('')
    
    # Output (G, g, h, (pi_h), A, B)

    return h, proof_list_setup
    
def commit(N, g, member):

    print('\n------------------------------------------------\n')
    print('Commit Phase')
    print('\n------------------------------------------------\n')
    
    
    a = []
    c = []

    ### Prepare
    
    # a_i <-sampling- B (uniform distribution)
    print('[+] Number of participants: ', member, '\n')
    
    for i in range(member):
        a_i = random.randrange(0, N)
        a.append(a_i)
        log.info(f"a_{i} is generated as {a_i}")
    
    # c_i <- g^a_i
    for i in range(member):
        c_i = pow(g, a[i], N)    # 연산량이 크지 않으므로 ** 사용
        c.append(c_i)
        log.info(f"c_{i} is generated as {c_i}")
    
    ### Commit(c_i, pi_i)
    
    # Publish c_i
    
    # ----- deadline T_1 -----
    
    ### Reveal(a_i)
    
    # Publish a_i
    
    
    ### Finalize({a'_i, c_i, d_i, pi_i)}^n_i=1
    
    # b* <- H(c_1||...||c_n)
    b_star = mod_hash_eth(N, *c)
    
    # print('[+] Input commits: ', commits)
    # b_star = int(b_star, 16)
    log.info('[+] b*: ', b_star)
    
    # For all j, Verify c_j = g^(a'_j) - else go to Recover
    # Omega = PI for i (h^H(c_i||b*))^(a'_i)
    

    print('[+] Commit list: ', c)

    return a, c, b_star
    
def reveal(N, h, a, c, b_star):

    print('\n------------------------------------------------\n')
    print('Reveal Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] Revealed Random list: ', a)    

    print('')
    
    # initialization
    omega = 1
    
    for i in range(len(a)):
        omega = ( omega*pow(pow(h, mod_hash_eth(N, c[i], b_star), N), a[i], N) ) % N
        
    print('[+] Revealed Random: ', omega, '\n')

    return omega
    
def recover(N, g, T, commits, b_star):

    ##### recovery scenario #####
    
    # Suppose None of Members Revealed Pessimistically
    # Omega = [PI for i c_i^H(c_i||b*) ]^(2^t)
    
    
    print('\n------------------------------------------------\n')
    print('Recovery Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] Suppose None of Members Revealed Pessimistically')
    
    """
    # initialization -> 이거 고치는 중
    omega = 1
    
    for i in range(member-len(recovery_index)):
        omega = (omega * pow( pow(h, int(hash(c[i], b_star), 16), N), a[i], N) ) % N

    """
    
    # recovery value initialization
    recov = 1
    
    for i in c:
        temp = pow(i, mod_hash_eth(N, i, b_star), N)
        recov = (recov * temp) % N
       
    # recov = simple_VDF(recov, N, T)
    
    start = time.time()
    omega_recov, exp_list_recov = VDF(N, recov, T, True)
    end = time.time()   
    print(f'[+] h for recover: {omega_recov} computed in {end - start:.5f} sec')
    print('')
    
    # Proof-of-Exponentiation proof & verification
    claim = construct_claim(exp_list_recov, N, recov, omega_recov, T)
    
    proof_list_recovery = gen_recursive_halving_proof(claim)
    print (f"[+] Prover submits the VDF proof:")
    print(*proof_list_recovery, sep='\n')
    
    # Wrong input test in the proof chain
    
    start = time.time()
    
    # This condition check is not necessary in this code, but for the real communication, the verifier should check if the proof used the same n, g, T 
    if N != proof_list_recovery[0][0] or recov != proof_list_recovery[0][1] or T != proof_list_recovery[0][3] :
        print('[-] Fail to Verification: Wrong proof base')
        print(proof_list_recovery[0])
        exit()
        
    
    test = verify_recursive_halving_proof(proof_list_recovery)   
    end = time.time()
    
    if (test==True):
        print(f"\n[+] Verification Success in {end - start:.5f} sec")
    else:
        print("\n[-] Fail to verification: Wrong Proof-of-Exponentiation")   
        exit()

    print('')    
        
        
    print('[+] Recovered random: ', omega_recov)
    
    print('\n\n\n[+] Tested Data:')
    print('(', end='')
    print(N, g, h, T, proof_list_setup, a, c, omega, omega_recov, proof_list_recovery, sep=',', end='')
    print(')')

    return omega_recov



if __name__=='__main__':


    ### Setup(l, t)
    
    # Run (G, g, A, B) <-sampling- GGen(l)
    
    
    print('Commit-Reveal-Recover Game Demo')
    #print('### Bicorn-RX Proof-of-Concept ###')
    print('-- Version 0.8\n\n')
    
    # User chooses a mode here
    mode_info = select_mode()    
    
    if mode_info["mode"] == "manual" or mode_info["mode"] == "test":
        N, g, T, member = mode_info['N'], mode_info['g'], mode_info['T'], mode_info['member']
        h, proof_list_setup = setup(N, g, T)
        a, c, b_star = commit(N, g, member)
        omega = reveal(N, h, a, c, b_star)
        recovered_omega = recover(N, g, T, c, b_star)
        
    elif mode_info["mode"] == "auto-setup":
        N, g, T = mode_info['N'], mode_info['g'], mode_info['T']
        h, proof_list_setup = setup(N, g, T)
        
        
    elif mode_info["mode"] == "auto-recover":
        N, g, T, commits, b_star = mode_info['N'], mode_info['g'], mode_info['T'], mode_info['commits'], mode_info['b_star']
        recovered_omega = recover(N, g, T, commits, b_star)
    
    
    
    

    
    
    
    
