import sys
import hashlib
import libnum
import math
import logging as log
import json
from datetime import datetime
from web3 import Web3

from web3_util import  mod_hash_eth, mod_hash_eth_128
from log_data import to_session_data_format, get_file_name_with_time



# utility function for number strings hash mod N
def mod_hash(n, *strings): 
    r = hashlib.sha3_256()
    input = ''.join(map(str, strings))
    r.update(input.encode('utf-8'))
    r.hexdigest()
    
    r=int.from_bytes(r.digest(), 'big')
    r=r%n
    
    return r

# VDF function: g^(2^T)
# Also, this function save every output into the list
# This is because the list is needed to generate a proof
# g^2^1, g^2^2, g^2^3, ....
# !!!! v is generated by this VDF so it should be changed when an efficient algorithm to generate v is added here !!!
def VDF(n, g, T, isExp=False):
    if(isExp):
        
        exp_list = []
        exp_list.append(g)
        
        for i in range(0,T):
            g = g*g % n
            # exp_list.append(g)
            
        return g, exp_list
            
    else:
        for i in range(0,T):
            g = g*g % n
        return g



# Efficiently calculate exponentiation using the precomputed list
# i.e.) 100 = (binary) 1100100 = 2^6 + 2^5 + 2^2

# !!!! it is found that this function is extremely slow!!!
# need to fix
def get_exp(exp_list, exp, n):
    res = 1
    
    logT = math.log2(exp)
    logT = math.floor(logT)
    for i in range(logT, -1, -1):
        temp = pow(2, i)
        test = exp/pow(2, i)
        if exp/pow(2, i) >= 1:
            res = res*exp_list[i] % n
            exp = exp - pow(2,i)
            
    return res


# need to develop : eval g, eval v
def eval_v(n, x, y, T):
    
    # what is the pattern of v?
    
    return v

# Generate a halving proof 
# Reference: https://eprint.iacr.org/2018/627.pdf Section 3.1 Page 8
# x is a generator g and y is the output of VDF
def gen_single_halving_proof(claim):
        
    n, x, y, T, v = claim
    
    # Use security parameter k as 128 bit
    r = mod_hash_eth_128(x, y, v) 
    log.info('generated r: ', r)
    
    x_prime = pow(x, r, n) * v % n
    
    # If T is odd, make the half of T even
    if T%2 == 0:
        T_half = int(T/2)
    else:
        T_half = int((T+1)/2)   
        y = y * y % n
    
    # As T increased by one, y should multiplied by the same amount (2^1)
    y_prime = pow(v, r, n) * y % n 

    log.info('y_prime: ', y_prime)
    log.info(f'x_prime^2^{T_half}: ', pow(x_prime, pow(2, T_half), n))
    
    # If T is odd, make the half of T even
    if T_half%2 == 0:
        T_quater = int(T_half/2)
    else:
        T_quater = int((T_half+1)/2)
        
    # in the current codes, VDF returns exp_list together        
    v_prime = VDF(n, x_prime, T_quater)
    
    
    log.info(f'v_prime^2^{T_quater}: ', pow(v_prime, pow(2, T_quater), n))
    
    # To make it non-interactive, Prover should send the random value r in the proof using Fiat-Shamir heuristic
    return (n, x_prime, y_prime, T_half, v_prime)



# Construct a full Proof-of-Exponentiation, Log2(T) size
def gen_recursive_halving_proof(claim):
    
    log.info(f"[+] Start to generate a proof for the claim \n{claim} \n")
    
    proof_list = [claim]
    T = claim[3]
    
    file_name = get_file_name_with_time("proof")
    f = open(file_name, "w")
    f.write("[")
    
    # generate & append a proof recursively till the proof outputs T = 1
    while T > 1:
        claim = gen_single_halving_proof(claim)
        T = claim[3]
        log.info(f"[+] Proof for T={T} is generated: {claim}")
        
        # this can make too large dictionary
        # proof_list.append(claim)
        
        # instead, we append to a file
        f.write("\n  ")  # indentation
        f.write(json.dumps(to_session_data_format(claim)))
        
        
    f.write("\n]")
        
    return proof_list





# Originally, for a claim, there is no need of the value 'v'
# But for the consistency of the resursive verification structure, we add 'v' to the claim
# VDF claim = (n, x, y, T, v)
# proof = (n, x_prime, y_prime, 2/T, v)        
def process_single_halving_proof(VDF_claim):
    
    n, x, y, T, v = VDF_claim
    
    log.info(f"...Verifying the proof for time {T}")
    
    if T == 1:
        check = pow(x, 2, n)
        if y == pow(x, 2, n):
            return True
        else:
            return False
    else:
        # check if the random value 'r' is well generated
        # r = sha(x, y, v) mod n
        # print('mod hash: ', mod_hash_eth(x, y, v))
        # print('mod hash / 2^128: ', int(mod_hash_eth(x, y, v) % pow(2, 128)))
        # test = input('stop: ')
        # Use security parameter k as 128 bit
        r = mod_hash_eth_128(x, y, v) 

        # check if the next proof is well contructed        
        x_prime = pow(x, r, n) * v % n
        
        # If T is odd, make the half of T even
        if T%2 == 0:
            T_half = int(T/2)
        else:
            T_half = int((T+1)/2)   
            y = y * y % n
            
        y_prime = pow(v, r, n) * y % n 
            
    return (n, x_prime, y_prime, T_half)

        
def verify_recursive_halving_proof(proof_list):
    
    proof_size = len(proof_list)

    # The output of one halving verficiation is the input of the next halving verification
    for i in range(0, proof_size):
        output = process_single_halving_proof(proof_list[i])
        
        # for debug, print proof and output to compare
        #if i+1 < proof_size:
            #print('Submitted Proof: ', proof_list[i+1][:-1])
            #print('Generated Output: ', output)
        
        if output == True:
            break
        
        elif output == False:
            log.warning('[-] Verification failed: The final proof returned False')
            return False
        
        # output does not contain the value 'v'
        elif output != proof_list[i+1][:-1]:
            log.warning('[-] Verification failed: The proof chain is invalid')
            log.warning(f'    invalid proof: {proof_list[i+1][:-1]}')
            return False

    return True



def VDF_test():
    
    test_n = 845 #131
    test_g = 12  #54
    test_T = 100 # T should be even ?
    test_y = VDF(test_n, test_g, test_T)
    
    # If T is odd, make the half of T even
    if test_T%2 == 0:
        test_T_half = int(test_T/2)
    else:
        test_T_half = int((test_T+1)/2)   
    
    test_v = get_exp(pow(2,test_T_half), test_n)
    
    claim = (test_n, test_g, test_y, test_T, test_v)
    proof_list = gen_recursive_halving_proof(claim)
    print(proof_list)
    test = verify_recursive_halving_proof(proof_list)
    print(test)
    

    
if __name__=='__main__':
    
    # VDF_test();
    
    # x=3 # security parameter lambda
    T=123
    bits=32
    
    if (len(sys.argv)>1):
        x=int(sys.argv[1])
    
    if (len(sys.argv)>2):
        T=int(sys.argv[2])
    
    if (len(sys.argv)>3):
        bits=int(sys.argv[3])
    
    
    # if (T>100): T=100
    
    N=libnum.generate_prime(bits)
    
    # to put random security parameter automatically here we use the time input
    now = datetime.now() # current date and time
    time = now.strftime("%H:%M:%S")
    
    g = hashlib.sha256(str(time).encode())
    g=int.from_bytes(g.digest(), 'big')
    g=g%N
       
    y, exp_list = VDF(N, g, T)
    
    # If T is odd, make the half of T even
    if T%2 == 0:
        T_half = int(T/2)
    else:
        T_half = int((T+1)/2)   
    
    v = get_exp(exp_list, pow(2,T_half), N)
    
    claim = (N, g, y, T, v)
    
    proof_list = gen_recursive_halving_proof(claim)
    print (f"\n[+] Prover computes and sends the chain of VDF proof={proof_list}\n\n")
    
    test = verify_recursive_halving_proof(proof_list)   
    
    
    if (test==True):
        print("\nVerifier confrimed that the prover computed correctly")
    else:
        print("\nVerifier rejects the prover's VDF claim")
