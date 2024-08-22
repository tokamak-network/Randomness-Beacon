# Copyright 2024 justin
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import math
import json
import time
from Pietrzak_VDF import VDF
from web3 import Web3
from sympy import *
import sys
sys.set_int_max_str_digits(100000) 
from log_data import val_to_big_number_dictionary
from datetime import datetime

def pad_hex(x):
    n = (64 - (len(x) % 64)) % 64
    return ('0' * n) + x

def hash_eth(*strings):
  # concatenate integer strings as even bytes
  # for example, [10, 17] -> 0x0a, 0x11 -> 0x0a11
  toHex = [format(int(x), '02x') for x in strings]
  padToEvenLen = [pad_hex(x) for x in toHex]
  input = ''.join(padToEvenLen)
  r = Web3.keccak(hexstr=input)
  # print(r.hex())
  r = int(r.hex(), 16)
  return r



def generate_proof(N, g, y, T):
    print('\nProof Generation------------------------------------------------\n')
    hM = hash_eth(g, y, T)
    print("H(m):",hM)
    mSB = 57896044618658097711785492504343953926634992332820282019728792003956564819968
    hM = hM | mSB
    l = nextprime(hM)

    exponent = pow(2,T) // l
    pi = pow(g, exponent, N)

    return l, pi


def verification(x, T, pi, l, N):
    r = pow(2, T, l)
    y = (pow(pi, l, N) * pow(x, r, N)) % N
    hM = hash_eth(x, y, T)
    mSB = 57896044618658097711785492504343953926634992332820282019728792003956564819968
    hM = hM | mSB
    if ( l == nextprime(hM) ):
        return True
    else:
        return False

def setup_with_verif_wesolowski(N, g, T):
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

    # Proof
    l, p = generate_proof(N, g, h, T)

    print("l: ", l)
    print("p: ", p)

    verification_result = verification(g, T, p, l, N)
    print("verification result: ", verification_result)
    if (verification_result == False):
        print("Verification failed")
        return
    keys = ['x', 'y', 'n', 'T', 'pi', 'l']
    data = {}
    data['x'] = val_to_big_number_dictionary(g)
    data['y'] = val_to_big_number_dictionary(h)
    data['n'] = val_to_big_number_dictionary(N)
    data['T'] = val_to_big_number_dictionary(T)
    data['pi'] = val_to_big_number_dictionary(p)
    data['l'] = val_to_big_number_dictionary(l)
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"./testLog/data_{current_time}_wesolowski.json"

    with open(file_name, 'w') as f:
        f.write(json.dumps(data, indent=2))
    print(f'[+] Data is saved in {file_name}')
    

