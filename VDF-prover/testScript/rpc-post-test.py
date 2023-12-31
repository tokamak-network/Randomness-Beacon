import requests
import json

url = "https://rpc.titan.tokamak.network"
headers = {'Content-Type': 'application/json'}

data = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",
    "params": ["0x049bF8C1291938Ae5A8CBB109062A91af3a153E5", "latest"],
    "id": 1
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.json())