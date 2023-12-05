import random
import hashlib
import time
import sys
import logging as log
from web3 import Web3


from Pietrzak_VDF import VDF, gen_recursive_halving_proof, verify_recursive_halving_proof, get_exp


### Unitility functions
def pad_hex(x):
    n = (64 - (len(x) % 64)) % 64
    return ('0' * n) + x

# keccack hash function outputs int for strings 
def mod_hash_eth(n, *strings):
  # concatenate integer strings as even bytes
  # for example, [10, 17] -> 0x0a, 0x11 -> 0x0a11
  toHex = [format(int(x), '02x') for x in strings]
  padToEvenLen = [pad_hex(x) for x in toHex]
  input = ''.join(padToEvenLen)
  r = Web3.keccak(hexstr=input)
  r = int(r.hex(), 16)
  r = r % n
  return r

    
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




if __name__=='__main__':
    

    ### Setup(l, t)
    
    # Run (G, g, A, B) <-sampling- GGen(l)
    
    a = []
    c = []
    
    T = 1000 # VDF를 위한 파라미터. 사전 연산을 예방하며 t에 비례한 시간이 소모됨
    N = 574124860045776250677760461775163599651322224153119109259455400887321364453863261321569207782210736007839174680839927021234474582257336368805224538101562837189035555129678385609799403965972091566161123366857070780717840822439991354140400800255059084900098763002924677244330526179226442655863576307898187480633022472982718091388580230012955561642086035134540717753475755091029885939798308279443281632368237618058506709130707267534300997300614380438224589755203523568399097274072410807062010611675101796907954608779304418438262261796442763907820433542865629328751329839954151183887425228850037508371075023529208535025609878648984897654788919032541906463453329993415850362679428637870461550053437593654857407409262047356904007386080137694446919150286956148176939053809880536495982696340382643000216950489972696406444742472613174712892786999987799145584142445250389997604320773414813284124130422189574749189122481411968263889751961673330736284300648464987815595304231334571235824446120159849747414371676164435310721878305600489626626806620054720547081774431305453734162505927347009225318413961349330311469729503697023633651626673651023121033950417164454110930459434671568486717578152953849284921713942325005283915668887804302741345899233 # 군(group)을 생성하기 위한 정수 크기 제한   
    member = 3  # 참여자 수


    print('\n   ___  _                       ___  _  __  ___       _____ \n \
      / _ )(_)______  _______  ____/ _ \| |/_/ / _ \___  / ___/ \n \
     / _  / / __/ _ \/ __/ _ \/___/ , _/>  <  / ___/ _ \/ /__  \n \
    /____/_/\__/\___/_/ /_//_/   /_/|_/_/|_| /_/   \___/\___/  \n')
    #print('### Bicorn-RX Proof-of-Concept ###')
    print('[+] Version 0.6\n\n')
    
    print('\n------------------------------------------------\n')
    print('Setup Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] PoC environment:')
    print('\t - Description of QR+ Group: ', N)
    print('\t - Time Delay for VDF (T): ', T)
    
    g = GGen(N)	
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
    print(f"[+] Prover submits the VDF proof:")
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
    
    ### Prepare()
    
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
    #commits = ''.join(map(str, c))
    b_star = mod_hash_eth(N, *c)
    
    # print('[+] Input commits: ', commits)
    # b_star = int(b_star, 16)
    log.info('[+] b*: ', b_star)
    
    # For all j, Verify c_j = g^(a'_j) - else go to Recover
    # Omega = PI for i (h^H(c_i||b*))^(a'_i)
    
    print('\n------------------------------------------------\n')
    print('Commit Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] Commit list: ', c)
    
    print('\n------------------------------------------------\n')
    print('Reveal Phase')
    print('\n------------------------------------------------\n')
    
    print('[+] Revealed Random list: ', a)    

    print('')
    
    # initialization
    omega = 1
    
    for i in range(member):
        omega = ( omega*pow(pow(h, mod_hash_eth(N, c[i], b_star), N), a[i], N) ) % N
        
    print('[+] Revealed Random: ', omega, '\n')
    
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
