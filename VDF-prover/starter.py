from web3 import Web3, HTTPProvider, Account
from web3.middleware import geth_poa_middleware
import configparser
import json
import os


        
def to_bytes_to_tuple(x, bitLen=20):
    x_bytes = x.to_bytes(32, byteorder='big')  # n을 32바이트로 변환
    bitLen = bitLen
    return (x_bytes, False, bitLen)


# config 파일을 읽어들임
config = configparser.ConfigParser()
config.read('config.ini')
networks = config['Networks']
contract_details = config['Contract']

# 환경 변수나 별도의 파일에서 개인 키를 가져옵니다.
private_key = os.getenv('MY_PRIVATE_KEY')

# RPC URL과 컨트랙트 정보 설정
rpc_url = networks['titan_goerli']
contract_address = contract_details['address']
contract_abi_file = contract_details['abi']

# Web3 인스턴스 생성 및 연결
w3 = Web3(HTTPProvider(rpc_url))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# ABI 파일 읽기
with open(contract_abi_file, 'r') as abi_file:
    contract_abi = json.load(abi_file)

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# 사용할 매개변수 설정
entrance_fee = int('1')  # Wei 단위 -> uint 256 에러 발생 !! 해결 방법 모름
commit_duration = 300  # 초 단위
commit_reveal_duration = 300  # 초 단위
n = to_bytes_to_tuple(566066687237)  # 예시 값


proofs = [
        [
            566066687237,
            193407962223,
            368572044080,
            60,
            215642181385
        ],
        [
            566066687237,
            533593194188,
            37890382725,
            30,
            182525232005
        ],
        [
            566066687237,
            533643009790,
            93189359466,
            15,
            5324410643
        ],
        [
            566066687237,
            179606067226,
            224794913883,
            8,
            321867976587
        ],
        [
            566066687237,
            11504243738,
            456796063102,
            4,
            402918426852
        ],
        [
            566066687237,
            123118694312,
            511630754025,
            2,
            438239359033
        ],
        [
            566066687237,
            79577448372,
            374051145201,
            1,
            374051145201
        ]
    ]  # 예시 배열
    
# 개인 키를 사용하여 계정 주소 가져오기
account = Account.from_key(private_key)

# 트랜잭션 생성
nonce = w3.eth.get_transaction_count(account.address)
#nonce = w3.eth.get_transaction_count(w3.eth.account.privateKeyToAccount(private_key).address)
transaction = contract.functions.start(entrance_fee, commit_duration, commit_reveal_duration, n, proofs).buildTransaction({
    'nonce': nonce,
    # 'gas': 100000,  # 필요에 따라 설정
    # 'gasPrice': w3.toWei('50', 'gwei')  # 필요에 따라 설정
})


# 트랜잭션 서명
signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

# 트랜잭션 전송
tx_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

# 트랜잭션 영수증을 얻기 위해 기다립니다.
receipt = w3.eth.waitForTransactionReceipt(tx_hash)

print(f'Transaction receipt: {receipt}')
