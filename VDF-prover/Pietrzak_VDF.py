import sys
import hashlib
import libnum
import math
import logging
import json
from datetime import datetime
from web3 import Web3
import time
import tempfile
import pickle
import os
from sympy import *

from web3_util import hash_eth_128
from log_data import to_session_data_format, get_file_name_with_time

logging.basicConfig(level=logging.INFO) # 기본 로깅 레벨 설정
log = logging.getLogger('Pietrzak_VDF')

# Utility function for number strings hash mod N
def mod_hash(n, *strings):
    r = hashlib.sha3_256()
    input = ''.join(map(str, strings))
    r.update(input.encode('utf-8'))
    r.hexdigest()

    r = int.from_bytes(r.digest(), 'big')
    r = r % n

    return r

# Save the exp_list
# def save_exp_list(exp_list, n, g, T, save_dir='exp_data'):
#     # Check and create the specified directory path
#     if not os.path.exists(save_dir):
#         os.makedirs(save_dir)
#
#     # Generate the file name
#     file_name = hashlib.sha256(f"{n}_{g}_{T}".encode()).hexdigest() + ".pkl"
#     file_path = os.path.join(save_dir, file_name)
#
#     # Save the exp_list results
#     with open(file_path, 'wb') as f:
#         pickle.dump(exp_list, f)
#     print(f"Location of the file where exp_list is saved: {file_path}")
#
# def load_exp_list(n, g, T, save_dir='exp_data'):
#     file_name = hashlib.sha256(f"{n}_{g}_{T}".encode()).hexdigest() + ".pkl"
#     file_path = os.path.join(save_dir, file_name)
#
#     # Load exp_list if the file exists
#     if os.path.isfile(file_path):
#         with open(file_path, 'rb') as f:
#             exp_list = pickle.load(f)
#         print(f"Loading exp_list from the file: {file_path}")
#         return exp_list
#     else:
#         return None

# VDF function: g^(2^T)
# Also, this function save every output into the list
# This is because the list is needed to generate a proof
# g^2^1, g^2^2, g^2^3, ....
def VDF(n, g, T, isExp=True):
    exp_list = []
    if isExp:
        exp_list.append(g)

    for i in range(0, T):
        g = g * g % n
        if isExp:
            exp_list.append(g)

    return g, exp_list


def get_exp(exp_list, exp, n):
    res = 1
    i = 0
    while exp > 0:
        if exp & 1:
            res = (res * exp_list[i]) % n
        exp >>= 1
        i += 1

    return res

def eval_v(n, x, T, r):
    i = 1
    sum_part = 0
    Z = Integer
    for j in range(2 ** (i - 1)):
        product_part = 1
        for k in range(1, i - 1):
            if (j % 2 ** k) > 0:
                product_part *= r[i - 1 - k]
        sum_part += product_part * pow(Z(2), ((T / Z(2) ** i) + j * pow(T, Z(2) ** (i - 1))))

    # Perform the final operation using the calculated sum_part
    v = pow(x, int(sum_part), n) % n

    return v



# Generate a halving proof
# Reference: https://eprint.iacr.org/2018/627.pdf Section 3.1 Page 8
# x is a generator g and y is the output of VDF
def gen_single_halving_proof(claim):
    n, x, y, T, v = claim

    # Use security parameter k as 128 bit
    r = hash_eth_128(x, y, v)

    x_prime = pow(x, r, n) * v % n
    # As T increased by one, y should multiplied by the same amount (2^1)
    y_prime = pow(v, r, n) * y % n

    # If T is odd, make the half of T even
    if T % 2 == 0:
        T_half = int(T / 2)
    else:
        T_half = int((T + 1) / 2)

    v = eval_v(n, x_prime, T_half, r)

    # To make it non-interactive, Prover should send the random value r in the proof using Fiat-Shamir heuristic
    return (n, x_prime, y_prime, T_half, v)


# Construct a full Proof-of-Exponentiation, Log2(T) size
def gen_recursive_halving_proof(claim):
    #log.info(f"[+] Start to generate a proof for the claim \n{claim} \n")

    proof_list = [claim]
    T = claim[3]

    # generate & append a proof recursively till the proof outputs T = 1
    while T > 1:
        claim = gen_single_halving_proof(claim)
        proof_list.append(claim)

        T = claim[3]
        #log.info(f"[+] Proof for T={T} is generated: {claim}")

    return proof_list


# Originally, for a claim, there is no need of the value 'v'
# But for the consistency of the resursive verification structure, we add 'v' to the claim
# VDF claim = (n, x, y, T, v)
# proof = (n, x_prime, y_prime, 2/T, v)
def process_single_halving_proof(VDF_claim):
    n, x, y, T, v = VDF_claim

    # log.info(f"...Verifying the proof for time {T}")

    if T == 1:
        check = pow(x, 2, n)
        if y == pow(x, 2, n):
            return True
        else:
            return False
    else:
        # check if the random value 'r' is well generated
        # r = sha(x, y, v) mod n
        # test = input('stop: ')
        # Use security parameter k as 128 bit
        r = hash_eth_128(x, y, v)

        # check if the next proof is well contructed
        x_prime = pow(x, r, n) * v % n

        # If T is odd, make the half of T even
        if T % 2 == 0:
            T_half = int(T / 2)
        else:
            T_half = int((T + 1) / 2)
            y = y * y % n

        y_prime = pow(v, r, n) * y % n

    return (n, x_prime, y_prime, T_half)


def verify_recursive_halving_proof(proof_list):
    proof_size = len(proof_list)

    # The output of one halving verficiation is the input of the next halving verification
    for i in range(0, proof_size):
        output = process_single_halving_proof(proof_list[i])

        # for debug, print proof and output to compare
        # if i+1 < proof_size:
        # print('Submitted Proof: ', proof_list[i+1][:-1])
        # print('Generated Output: ', output)

        if output == True:
            break

        elif output == False:
            log.warning('[-] Verification failed: The final proof returned False')
            return False

        # output does not contain the value 'v'
        elif output != proof_list[i + 1][:-1]:
            log.warning('[-] Verification failed: The proof chain is invalid')
            log.warning(f'invalid proof: {proof_list[i + 1][:-1]}')
            return False

    return True

if __name__ == '__main__':
    start_time = time.time()
    start_VDF_evaluation = time.time()
    T = 2 ** 20
    bits = 512

    if (len(sys.argv) > 1):
        x = int(sys.argv[1])

    if (len(sys.argv) > 2):
        T = int(sys.argv[2])

    if (len(sys.argv) > 3):
        bits = int(sys.argv[3])

    # if (T>100): T=100

    # p = 10000007
    # q = 10000037
    # N = p * q  # Example modulus
    N = libnum.generate_prime(bits)
    g = pow(2, 6) % N  # Example base

    # to put random security parameter automatically here we use the time input
    # g = hashlib.sha256(str(time).encode())
    # g = int.from_bytes(g.digest(), 'big')
    # g = g % N
    # start_VDF_evaluation = time.time()
    y, exp_list = VDF(N, g, T)

    # If T is odd, make the half of T even
    if T % 2 == 0:
        T_half = int(T / 2)
    else:
        T_half = int((T + 1) / 2)

    v = get_exp(exp_list, pow(2, T_half), N)
    r = hash_eth_128(g, y, v)

    end_VDF_evaluation = time.time()
    execution_VDF_evaluation = end_VDF_evaluation - start_VDF_evaluation


    claim = (N, g, y, T, v)
    start_time_gen_proof = time.time()
    proof_list = gen_recursive_halving_proof(claim)
    end_time_gen_proof = time.time()
    execution_time_gen_proof = end_time_gen_proof - start_time_gen_proof

    print(f"\n[+] Prover computes and sends the chain of VDF proof={proof_list}\n\n")

    start_time_verify_proof = time.time()
    test = verify_recursive_halving_proof(proof_list)
    end_time_verify_proof = time.time()
    execution_time_verify_proof = end_time_verify_proof - start_time_verify_proof
    print(f"Execution time of VDF evaluation: {execution_VDF_evaluation} seconds")
    print(f"Execution time of gen_recursive_halving_proof: {execution_time_gen_proof} seconds")
    print(f"Execution time of verify_recursive_halving_proof: {execution_time_verify_proof} seconds")

    if (test == True):
        print("\nVerifier confrimed that the prover computed correctly")
    else:
        print("\nVerifier rejects the prover's VDF claim")

    end_time = time.time()  # 실행 종료 시간 측정
    total_time = end_time - start_time  # 전체 실행 시간 계산

    print(f"\n[+] 전체 실행 시간: {total_time:.2f}초")
