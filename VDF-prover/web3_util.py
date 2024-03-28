from web3 import Web3
import configparser
import json

DEFAULT_NETWORK = 'sepolia_testnet'


def pad_hex(x):
    n = (64 - (len(x) % 64)) % 64
    return ('0' * n) + x
    
# keccack 256 hash function outputs int for strings 
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
  
# return last 128 bit from keccack 256 hash function outputs int for strings 
def hash_eth_128(*strings):
  r = hash_eth(*strings)
  #r = r % pow(2, 128)
  r = r >> 128
  return r

def read_config():
    """Read and return configuration from a file."""
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Networks'], config['Contract']

def get_web3(rpc_url):
    """Initialize and return a Web3 instance with the given RPC URL."""
    return Web3(Web3.HTTPProvider(rpc_url))

def select_network(networks, contract_details):
    """Prompt the user to select a network and return the corresponding Web3 instance."""
    print(f"Select a network for the contract address {contract_details['address']}:")
    print("1. Ethereum Mainnet")
    print("2. Ethereum Sepolia Testnet")
    print("3. Titan (Layer 2) Mainnet")
    print("4. Titan (Layer 2) Goerli Testnet")
    choice = input("Choice: ")
    print("")

    if choice == "1":
        return get_web3(networks['ethereum_mainnet'])
    elif choice == "2":
        return get_web3(networks['sepolia_testnet'])
    elif choice == "3":
        return get_web3(networks['titan_mainnet'])
    elif choice == "4":
        return get_web3(networks['titan_goerli'])
    else:
        print("Invalid selection. Please try again.")
        return select_network(networks)

def setup_contract(web3, contract_details):
    """Create and return a contract object using the provided Web3 instance."""
    with open(contract_details['abi'], 'r') as abi_file:
        contract_abi = json.load(abi_file)
    contract_address = Web3.to_checksum_address(contract_details['address'])
    return web3.eth.contract(address=contract_address, abi=contract_abi)
    

def get_commit_reveal_values(contract, round_number):
    """Retrieve all getCommitRevealValues for a given round until an empty participant address is found."""
    commit_reveal_values = []
    index = 0
    while True:
        value = contract.functions.getCommitRevealValues(round_number, index).call()
        # participantAddress가 '0x000...'인 경우 더 이상의 유효한 값이 없다고 간주
        if value[2] == '0x0000000000000000000000000000000000000000':
            break
        commit_reveal_values.append(value)
        index += 1
    return commit_reveal_values
    
def get_stage(stage_value):
    """Convert stage value to stage name."""
    stages = ["Finished", "Commit", "Reveal"]
    return stages[stage_value] if stage_value < len(stages) else "Unknown"
    
def parse_commits(commit_reveal_values):
    """Parse commit reveal values and return as a list of dictionaries."""
    parsed_data = []
    """
    for value in commit_reveal_values:
        parsed_entry = {
            "c": value[0],
            "a": value[1],
            "participantAddress": value[2]
        }
        parsed_data.append(parsed_entry)
    """
    for value in commit_reveal_values:
        parsed_data.append(value[0])
    return parsed_data

def parse_general_values_at_round_v2(values_at_round):
    """Parse a ValueAtRound struct and return as a dictionary."""
    return {
        "startTime": values_at_round[0],
        "numOfPariticipants": values_at_round[1],
        "count": values_at_round[2],
        "consumer": values_at_round[3],
        "bStar": values_at_round[4],
        "commitsString": values_at_round[5],
        "omega": values_at_round[6],
        "stage": values_at_round[7],
        "isCompleted": values_at_round[8],
        "isAllRevealed": values_at_round[9]
    }
    
def parse_general_values_at_round(values_at_round):
    """Parse a ValueAtRound struct and return as a dictionary."""
    return {
        "numOfParticipants": values_at_round[0],
        "count": values_at_round[1],
        "bStar": values_at_round[2],
        "commitsString": values_at_round[3],
        "omega": values_at_round[4],
        "stage": values_at_round[5],
        "isCompleted": values_at_round[6],
        "isAllRevealed": values_at_round[7]
    }

##(NBITLEN, GBITLEN, HBITLEN, NVAL, GVAL, HVAL);
def parse_setup_values_at_round_v2(values_at_round):
    """Parse a ValueAtRound struct and return as a dictionary."""
    return {
        "T": values_at_round[0],
        "nBitLen": values_at_round[1],
        "gBitLen": values_at_round[2],
        "hBitLen": values_at_round[3],
        "nVal": values_at_round[4],
        "gVal": values_at_round[5],
        "hVal": values_at_round[6]
    }
    
def parse_setup_values_at_round(values_at_round):
    """Parse a ValueAtRound struct and return as a dictionary."""
    return {
        "setUpTime": values_at_round[0],
        "commitDuration": values_at_round[1],
        "commitRevealDuration": values_at_round[2],
        "T": values_at_round[3],
        "proofSize" : values_at_round[4],
        "n": values_at_round[5],
        "g": values_at_round[6],
        "h": values_at_round[7]
    }

def get_contract_values_v2(round=None):
    networks, contract_details = read_config()

    print('The setting from config.ini:')
    print('\t Network: ', contract_details['network'])
    print('\t Contract Address: ', contract_details['address'])
    web3 = Web3(Web3.HTTPProvider(networks[contract_details['network']]))
    contract = setup_contract(web3, contract_details)

    if(round==None):
        """Read and return specific values from the smart contract."""
        print('\n[+] There no input for option \'round\' so fetch the round information from the contract .... \n')
        round_info = contract.functions.getNextRound().call()
        if round_info > 0:
            round_info = round_info - 1
    else:
        round_info = round
    raw_general_values_at_round = contract.functions.getValuesAtRound(round_info).call()
    genearl_values_at_round = parse_general_values_at_round_v2(raw_general_values_at_round)
    stage = get_stage(genearl_values_at_round['stage'])
    print("stage", stage)

    
    raw_setup_values_at_round = contract.functions.getSetUpValues().call()
    setup_values_at_round = parse_setup_values_at_round_v2(raw_setup_values_at_round)
    genearl_values_at_round.update(setup_values_at_round)
    values_at_round = genearl_values_at_round

    commit_reveal_values = get_commit_reveal_values(contract, round_info)
    commits = parse_commits(commit_reveal_values)

    return round_info, stage, values_at_round, commits

def get_contract_values(round=None):
    networks, contract_details = read_config()
    
    print('The setting from config.ini:')
    print('\t Network: ', contract_details['network'])
    print('\t Contract Address: ', contract_details['address'])    
      
    web3 = Web3(Web3.HTTPProvider(networks[contract_details['network']]))
    contract = setup_contract(web3, contract_details)
    
    if(round==None):
        """Read and return specific values from the smart contract."""
        print('\n[+] There no input for option \'round\' so fetch the round information from the contract .... \n')
        round_info = contract.functions.randomAirdropRound().call()
        
    else:
        round_info = round

    # getValuesAtRound 정보 가져오기 및 파싱
    raw_general_values_at_round = contract.functions.getValuesAtRound(round_info).call()
    genearl_values_at_round = parse_general_values_at_round(raw_general_values_at_round)
    stage = get_stage(genearl_values_at_round['stage'])
    print("stage", stage)
    # print('genearl_values_at_round: ', genearl_values_at_round)
    
    raw_setup_values_at_round = contract.functions.getSetUpValuesAtRound(round_info).call()
    setup_values_at_round = parse_setup_values_at_round(raw_setup_values_at_round)
    # print('genearl_values_at_round: ', print(setup_values_at_round))
    genearl_values_at_round.update(setup_values_at_round)
    values_at_round = genearl_values_at_round

    # getCommitRevealValues 정보 가져오기 및 파싱
    commit_reveal_values = get_commit_reveal_values(contract, round_info)
    commits = parse_commits(commit_reveal_values)

    return round_info, stage, values_at_round, commits




if __name__ == "__main__":
    c = ['10', '11']
    # c = even_hex_concat(c)
    print(c)
    # get_contract_values()
