import random
import libnum
import hashlib
import argparse
import time
import sys
import logging as log
import json
from datetime import datetime
from web3 import Web3

from Web3_util import  get_contract_values, mod_hash_eth

from Pietrzak_VDF import VDF, gen_recursive_halving_proof, verify_recursive_halving_proof, get_exp

from Commit_Reveal_Recover import setup, commit, reveal, recover, generate_divisor, GGen



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
            print()
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
                "mode": "manual",
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
                "mode": "test",
                "N": N,
                "g": g,
                "T": T,
                "member": member
            }
        
    else:
        print("Invalid selection. Please try again.")
        select_mode()



if __name__=='__main__':


    ### Setup(l, t)
    
    # Run (G, g, A, B) <-sampling- GGen(l)
    
    
    print('Commit-Reveal-Recover Game Demo')
    #print('### Bicorn-RX Proof-of-Concept ###')
    print('-- Version 0.8\n\n')
    
    # User chooses a mode here
    mode_info = select_mode()   

    print('mode_info:', mode_info)
    print('mode_info[mode]:', mode_info["mode"])
    
    if mode_info["mode"] == "manual" or mode_info["mode"] == "test":
        N, g, T, member = mode_info['N'], mode_info['g'], mode_info['T'], mode_info['member']
        
        h, proof_list_setup = setup(N, g, T)
        print('setup complete')
        a, c, b_star = commit(N, g, member)
        print('commit complete')
        omega = reveal(N, h, a, c, b_star)
        print('reveal complete')
        recovered_omega, proof_list_recovery = recover(N, g, T, c, b_star)
        print('recover complete')
        
        tested_data = {
            "N": N,
            "g": g,
            "h": h,
            "T": T,
            "proof_list_setup": proof_list_setup,
            "a": a,
            "c": c,
            "omega": omega,
            "recovered_omega": recovered_omega,
            "proof_list_recovery": proof_list_recovery
        }

        # Printing the data as before
        print('\n\n\n[+] Tested Data:')
        print('(', end='')
        print(N, g, h, T, proof_list_setup, a, c, omega, recovered_omega, proof_list_recovery, sep=',', end='')
        print(')')

        # Format the current time as YYYYMMDD_HHMMSS
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"./testlog/data_{current_time}.json"

        # Writing the data to a JSON file
        with open(file_name, 'w') as file:
            json.dump(tested_data, file, indent=4)
        
        print(f'[+] Tested Data is saved as {file_name}')
        
    elif mode_info["mode"] == "auto-setup":
        N, g, T = mode_info['N'], mode_info['g'], mode_info['T']
        h, proof_list_setup = setup(N, g, T)
        
        
    elif mode_info["mode"] == "auto-recover":
        N, g, T, commits, b_star = mode_info['N'], mode_info['g'], mode_info['T'], mode_info['commits'], mode_info['b_star']
        recovered_omega = recover(N, g, T, commits, b_star)
    
    
    
    

    
    
    
    
