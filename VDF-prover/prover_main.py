import random
import libnum
import hashlib
import configparser
import argparse
import time
import sys
import logging as log
import json

from web3_util import  get_contract_values, get_contract_values_v2

from log_data import log_session_data, log_session_data2

from Pietrzak_VDF import VDF, gen_recursive_halving_proof, verify_recursive_halving_proof, get_exp

from Commit_Reveal_Recover import setup_without_verif, recover_without_verif, setup, commit, reveal, recover, generate_divisor, GGen


def select_fixed_setup_recover_mode(round):
    round_info, stage, value_at_round, commits = get_contract_values_v2(round)

    if stage != "Finished":
        print()
        print(f'[+] Round {round_info} is active with Stage {stage}')
        ans = input(f'Do you want to recover RANDOM for Round {round_info}? (y or n):')

        if ans.lower() == 'y':
            n = value_at_round['nVal']
            g = value_at_round['gVal']
            T = 4194304
            h = value_at_round['hVal']
            commits = commits

            return {
                "mode": "fixed-setup-recover",
                "n": n,
                "g": g,
                "T": T,
                "h": h,
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
    parser.add_argument('-m', '--mode', choices=['auto', 'setup', 'test', 'recover', 'testDiffCommitLen'], required=True, help="Mode of operation: auto, setup, or test.")
    parser.add_argument('-r', '--round', type=int, help="Round number for auto mode.")
    parser.add_argument('-b', '--bit_size', type=int, help="Modulo bit size for setup mode.")
    parser.add_argument('-d', '--time_delay', type=int, help="VDF time delay for setup mode.")
    parser.add_argument('-cl', '--commit_len', type=int, help="Commit length for test mode.")
    args = parser.parse_args()

    # Read configuration file if mode is auto
    if args.mode == 'auto':
        return select_automatic_mode(args.round)
    
    elif args.mode == 'recover':
        return select_fixed_setup_recover_mode(args.round)

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
        n = generate_divisor(2048) #1024, 2048, 3072
        g = GGen(n)
        T = 33554432 #1048576, 2097152, 4194304, 8388608, 16777216, 33554432
        member = 3
        return {
                "mode": "test",
                "n": n,
                "g": g, 
                "T": T,
                "member": member
            }
    elif args.mode == 'testDiffCommitLen':
        n = 16787733290935122481437368133728328346576090632807129741527596642736905263844061000187347139315317854842649687790400123842298700426880474722304214883554816375292570757037140621378906385135613539582479043084244392163803829650051309553263880814324743421183907069761513779523295519767850770757782996347391782717727477920209304326136439376945841495526774917149836500875659771739375305606741462825529564666845086594751156082560955283183033943754755747751029228508120785017448871928365327311734007107017088983210531036030794782231712191306094543432182670132968253513609642276459210688739863575743598266362835007740972451509
        g = 12543942723415074726965043504991922076121696907821570137511397704577331244629576103672491151224439340943004908229679369031717029621690273353987597803140646282617628831108275423342904110725502150362277771037719189200216177137767892855999953212790783564996680919349203815527997669865940950647441505927180094446092180376090792192854326534733972281624935103155199270807833250749049472729079797267656994138805514016533206241588951257796936214597710332091745495056825768914112252468642159294549416963625054717596085886516948142775845170467185469231731884552275770242388599901121679147636866203131493729464443405551467582277
        T = 4194304
        member = args.commit_len
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
    
    elif mode_info["mode"] == "fixed-setup-recover":
        n, g, T, commitListHex = mode_info['n'], mode_info['g'], mode_info['T'], mode_info['commits']
        
        # binary in array to int decimal
        # i.e., n = {b'\x01\x02', 9}
        n = int.from_bytes(n, 'big')
        g = int.from_bytes(g, 'big')
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
        log_session_data2(mode_info["mode"], sessionData)

    
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