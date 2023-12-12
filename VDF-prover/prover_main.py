import random
import libnum
import hashlib
import argparse
import time
import sys
import logging as log
import json

from Web3_util import  get_contract_values, mod_hash_eth

from log_data import log_game_data

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
            n = generate_divisor(bitsize)
            g = GGen(n)	
            print()
            T = int(input("Input time delay (Over 100000 is recommended): "))
            
            return {
                "mode": "auto-setup",
                "n": n,
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
            n = value_at_round['n']
            g = value_at_round['g']
            T = value_at_round['T']
            bstar = value_at_round['bStar']
            commits = commits
            
            return {
                "mode": "auto-recover",
                "n": n,
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
    print("Select a mode (1/2/3/4):")
    print("1. Manual: A user manually inputs numbers")
    print("2. Automatic (Recommended): This program gets inputs from the smart contract on the Ethereum compatible network")
    print("3. Use the default test option (256RSA, 0.001s delay)")
    print("4. Use the default test option (For test, 2048RSA, 1s delay)")
    choice = input("Choose: ")
    print()

    if choice == "1":
        bitsize = int(input("Input bit size (2048 is recommended): "))
        n = generate_divisor(bitsize)
        g = GGen(n)
        T = int(input("Input time delay (Over 10000000 is recommended): "))
        member = int(input("Input number of members: "))
        return {
                "mode": "manual",
                "n": n,
                "g": g,
                "T": T,
                "member": member
            }
        
    elif choice == "2":
        return select_automatic_mode()
        
    elif choice == "3":
        n = generate_divisor(256) #256
        g = GGen(n)
        T = 100
        member = 3
        return {
                "mode": "test",
                "n": n,
                "g": g,
                "T": T,
                "member": member
            }
            
    elif choice == "4":
        n = generate_divisor(2048)
        g = GGen(n)
        T = 1000
        member = 3
        return {
                "mode": "test",
                "n": n,
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
    print('-- Version 0.9\n\n')
    
    # User chooses a mode here
    mode_info = select_mode()   

    print('mode_info:', mode_info)
    print('mode_info[mode]:', mode_info["mode"])
    
    if mode_info["mode"] == "manual" or mode_info["mode"] == "test":
        n, g, T, member = mode_info['n'], mode_info['g'], mode_info['T'], mode_info['member']
        
        h, setupProofs = setup(n, g, T)
        print('setup complete')
        randomList, commitList, b_star = commit(n, g, member)
        print('commit complete')
        omega = reveal(n, h, randomList, commitList, b_star)
        print('reveal complete')
        recoveredOmega, recoveryProofs = recover(n, g, T, commitList, b_star)
        print('recover complete')
        
        gameData = {
            'n': n,
            'g': g,
            'h': h,
            'T': T,
            'setupProofs': setupProofs,
            'randomList': randomList,
            'commitList': commitList,
            'omega': omega,
            'recoveredOmega': recoveredOmega,
            'recoveryProofs': recoveryProofs
        }
        
        # the log is printed in two ways
        # 1. print on terminal
        # 2. print as a JSON-like file
        # i.e. { n : "0x123" }
        # so it can be imported to js test scripts directly
        log_game_data(gameData)
        
    elif mode_info["mode"] == "auto-setup":
        n, g, T = mode_info['n'], mode_info['g'], mode_info['T']
        h, setupProofs = setup(n, g, T)
        
        
    elif mode_info["mode"] == "auto-recover":
        n, g, T, commits, b_star = mode_info['n'], mode_info['g'], mode_info['T'], mode_info['commits'], mode_info['b_star']
        recoveredOmega = recover(n, g, T, commits, b_star)
    
    
    
    

    
    
    
    
