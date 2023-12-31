import json
from datetime import datetime

# encoder for the custom json-like format
# depreciated!
class NoQuoteEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False, indent_level=0):
        indent_space = '  ' * indent_level
        if isinstance(o, dict):
            yield '{\n'
            first = True
            for key, value in o.items():
                if not first:
                    yield ',\n'
                yield indent_space + '  ' + key + ': '
                yield from self.iterencode(value, indent_level=indent_level + 1)
                first = False
            yield '\n' + indent_space + '}'
        elif isinstance(o, list):
            yield '[\n'
            first = True
            for value in o:
                if not first:
                    yield ',\n'
                yield indent_space + '  '
                yield from self.iterencode(value, indent_level=indent_level + 1)
                first = False
            yield '\n' + indent_space + ']'
        else:
            yield from super(NoQuoteEncoder, self).iterencode(o, _one_shot)
            
            
            
# 3 -> b11 -> 2
# 4 -> b100 -> 3        
def get_bitlen_from_hex(val):
    return val.bit_length()

# This function converts a demiaml to a padded hex string to make it have 256-bits scale length     
# for example, 123456789 -> '0x00000000000000000000000000000000000000000000000000000000075bcd15'
def decimal_to_padded_hex(decimal_number):
    # Convert the decimal number to a hexadecimal string and remove the '0x' prefix
    hex_string = hex(decimal_number)[2:]

    # Calculate the padding length to make the length a multiple of 64
    padding_length = 64 - (len(hex_string) % 64)
    if padding_length == 64:
        padding_length = 0

    # Pad the string with leading zeros
    padded_hex_string = '0x' + '0' * padding_length + hex_string

    return padded_hex_string
 

# big number structure example
# {
#  "val": "0x6c02e134e08a774687da0c8d93cde935b0f7b4f817b876bbc898f0219dc6d965bf3152ceec51a9e19a2138a3a8809ed6a6bd9ce06a66c9909de72bf6bc7c667671abc9a82e953ca5fb919d0d535238dcd8d9562b4bba6b52bae30973d3ede112d5a75a84b23e160744c23d7f9028a7267ca581ab1743e597230605208838d95e07e9552aaea993ff41925489c488d53e2bbbb7970b16bf0cf483789364467513b9178b8eae61ace37524daf96b2fb40880e758240f9a16bc87d1f485d7f815893d12743e987e6da815dad1924b4643925e32ed742a7f7e86ddd30f9d7318a2848c43ce7ee2800564b2d7fe8fb1b7dc82f1f9c8c2e3029c7637a8a80fa1699b7b",
#  "bitlen": 2047
# }
def val_to_big_number_dictionary(decimal_number):
    new_dic = {"val": decimal_to_padded_hex(decimal_number), "bitlen": get_bitlen_from_hex(decimal_number) }
    return new_dic
    
    
def to_session_data_format(claim):
    
    # change the proof list to dictionary
    keys = ['n', 'x', 'y', 'T', 'v']
    
    claim = dict(zip(keys, claim))
        
    # change the big decimal numbers as a hex-string 
    # in the nested dictionary except for the key 't'
    for key in claim:

        if key == 'T':
            pass
                
        else: # key == 'n' or key == 'x' or key == 'y' or key == 'v':
            claim[key] = val_to_big_number_dictionary(claim[key])
        
    return claim


def get_file_name_with_time(mode):
    # Format the current time as YYYYMMDD_HHMMSS
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"./testlog/data_{current_time}_{mode}.json"
    
    return file_name

def log_session_data(mode, sessionData):
    
    # change the proof list to dictionary
    keys = ['n', 'x', 'y', 'T', 'v']
    
    if 'setupProofs' in sessionData:
        for i in range(len(sessionData['setupProofs'])):
            new_element = dict(zip(keys, sessionData['setupProofs'][i]))
            sessionData['setupProofs'][i] = new_element
        
    if 'recoveryProofs' in sessionData:
        for i in range(len(sessionData['recoveryProofs'])):
            new_element = dict(zip(keys, sessionData['recoveryProofs'][i]))
            sessionData['recoveryProofs'][i] = new_element
        
    # change the big decimal numbers as a hex-string 
    # in the nested dictionary except for the key 't'
    for key in sessionData:

        if key == 'T':
            pass
        elif key == 'setupProofs' or key == 'recoveryProofs':
            for i in range(len(sessionData[key])):
                for innerKey in sessionData[key][i]:
                    if innerKey != 'T':
                        sessionData[key][i][innerKey] = val_to_big_number_dictionary(sessionData[key][i][innerKey])
                        
        elif key == 'randomList' or key == 'commitList':
            for i in range(len(sessionData[key])):
                sessionData[key][i] = val_to_big_number_dictionary(sessionData[key][i])
                
        else: # key == 'n' or key == 'x' or key == 'y' or key == 'v':
            sessionData[key] = val_to_big_number_dictionary(sessionData[key])
        
    
    # 1. print data on terminal
    print('\n\n\n[+] Game Data: ', json.dumps(sessionData, indent=2))

    # 2. print data as a JSON-like file
    # encoded_data = ''.join(NoQuoteEncoder().iterencode(sessionData))
    
    # Format the current time as YYYYMMDD_HHMMSS
    file_name = get_file_name_with_time(mode)

    # Writing the data to a JSON file
    with open(file_name, 'w') as file:
        file.write(json.dumps(sessionData, indent=2))
    
    print('\n\n')
    print(f'[+] Session Data is saved as {file_name}')