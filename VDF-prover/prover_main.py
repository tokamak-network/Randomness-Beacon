import random
import libnum
import hashlib
import configparser
import argparse
import time
import sys
import logging as log
import json

from web3_util import  get_contract_values, mod_hash_eth

from log_data import log_session_data

from Pietrzak_VDF import VDF, gen_recursive_halving_proof, verify_recursive_halving_proof, get_exp

from Commit_Reveal_Recover import setup_without_verif, recover_without_verif, setup, commit, reveal, recover, generate_divisor, GGen




def select_automatic_mode(round):
    round_info, stage, value_at_round, commits = get_contract_values(round)

    if stage != "Finished":
        print()
        print(f'[+] Round {round_info} is active with Stage {stage}')
        ans = input(f'Do you want to recover RANDOM for Round {round_info}? (y or n):')
        
        if ans.lower() == 'y':
            n = value_at_round['n']
            g = value_at_round['g']
            T = value_at_round['T']
            h = value_at_round['h']
            bstar = value_at_round['bStar']
            commits = commits
            
            return {
                "mode": "auto-recover",
                "n": n,
                "g": g,
                "T": T,
                "h": h,
                "bstar": bstar,
                "commits": commits
            }
            
            
        elif ans.lower() == 'n':
            print('\n\n')
            print('[+] Then this script terminates.') 
            exit()
            
        else:
            print("Invalid selection. Please try again.")
            select_automatic_mode()
    
    print(f'[+] Round {round_info} of the contract does not need recovery.') 
    exit() 
    

        

def command_parser():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run the script based on the provided mode and configuration.")
    parser.add_argument('-m', '--mode', choices=['auto', 'setup', 'test'], required=True, help="Mode of operation: auto, setup, or test.")
    parser.add_argument('-r', '--round', type=int, help="Round number for auto mode.")
    parser.add_argument('-b', '--bit_size', type=int, help="Modulo bit size for setup mode.")
    parser.add_argument('-d', '--time_delay', type=int, help="VDF time delay for setup mode.")
    args = parser.parse_args()

    # Read configuration file if mode is auto
    if args.mode == 'auto':
        return select_automatic_mode(args.round)

    elif args.mode == 'setup':
        if not all([args.bit_size, args.time_delay]):
            print("All setup mode arguments (-b, -d) are required.")
            return
        n = generate_divisor(args.bit_size)
        g = GGen(n)

        return {
                "mode": "setup",
                "n": n,
                "g": g,
                "T": args.time_delay,
            }

    elif args.mode == 'test':
        n = generate_divisor(2048)
        g = GGen(n)
        T = 100000
        member = 3
        return {
                "mode": "test",
                "n": n,
                "g": g,
                "T": T,
                "member": member
            }


    else:
        print("Invalid mode selected.")
        return



if __name__=='__main__':


    ### Setup(l, t)
    
    # Run (G, g, A, B) <-sampling- GGen(l)
    
    
    print('Commit-Reveal-Recover Game Demo')
    #print('### Bicorn-RX Proof-of-Concept ###')
    print('-- Version 1.0\n\n')
    
    # User chooses a mode here
    mode_info = command_parser()
    # mode_info = select_mode()   

    # print('mode_info:', mode_info)
    print('mode_info[mode]:', mode_info["mode"])
    
        
    if mode_info["mode"] == "auto-recover":
        n, g, T, commitListHex = mode_info['n'], mode_info['g'], mode_info['T'], mode_info['commits']
        
        # binary in array to int decimal
        # i.e., n = {b'\x01\x02', 9}
        n = int.from_bytes(n[0], 'big')
        g = int.from_bytes(g[0], 'big')
        T = T
        commitList = []
        for i in commitListHex:
            commitList.append(int.from_bytes(i[0], 'big'))
        
        recoveredOmega, recoveryProofs = recover_without_verif(n, g, T, commitList)
        
        sessionData = {
            'recoveryProofs': recoveryProofs
        }
        
        # the log is printed in two ways
        # 1. print on terminal
        # 2. print as a JSON file
        # so it can be imported to js test scripts directly
        log_session_data(mode_info["mode"], sessionData)
    

    
    elif mode_info["mode"] == "setup":
        n, g, T = mode_info['n'], mode_info['g'], mode_info['T']
        
        h, setupProofs = setup(n, g, T)
        """
        randomList, commitList, b_star = commit(n, g, member)
        print('commit complete')
        omega = reveal(n, h, randomList, commitList, b_star)
        print('reveal complete')
        recoveredOmega, recoveryProofs = recover(n, g, T, commitList, b_star)
        print('recover complete')
        """
        
        sessionData = {
            'n': n,
            'g': g,
            'h': h,
            'T': T,
            'setupProofs': setupProofs
        }
        
        log_session_data(mode_info["mode"], sessionData)
        
    elif mode_info["mode"] == "auto-setup":
        n, g, T = mode_info['n'], mode_info['g'], mode_info['T']
        h, setupProofs = test_setup(n, g, T)
        
        sessionData = {
            'n': n,
            'g': g,
            'h': h,
            'T': T,
            'setupProofs': setupProofs
        }
        
        log_session_data(mode_info["mode"], sessionData)
        

    
    elif mode_info["mode"] == "test":
        n, g, T, member = mode_info['n'], mode_info['g'], mode_info['T'], mode_info['member']
        
        h, setupProofs = setup_without_verif(n, g, T)
        print('setup complete')
        
        randomList, commitList, b_star = commit(n, g, member)
        print('commit complete')
        omega = reveal(n, h, randomList, commitList, b_star)
        print('reveal complete')
        recoveredOmega, recoveryProofs = recover(n, g, T, commitList, b_star)
        print('recover complete')
        
        sessionData = {
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
        
        log_session_data(mode_info["mode"], sessionData)