import json
from datetime import datetime


class NoQuoteEncoder(json.JSONEncoder):
    def iterencode(self, o, _one_shot=False):
        if isinstance(o, dict):
            yield '{'
            first = True
            for key, value in o.items():
                if not first:
                    yield ', '
                yield key + ': '
                yield from self.iterencode(value)
                first = False
            yield '}'
        elif isinstance(o, list):
            yield '['
            first = True
            for value in o:
                if not first:
                    yield ', '
                yield from self.iterencode(value)
                first = False
            yield ']'
        else:
            yield from super(NoQuoteEncoder, self).iterencode(o)

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
    


def log_game_data(gameData):
    
    # change the proof list to dictionary
    keys = ['n', 'x', 'y', 'T', 'v']
    
    for i in range(len(gameData['setupProofs'])):
        new_element = dict(zip(keys, gameData['setupProofs'][i]))
        gameData['setupProofs'][i] = new_element
        
    for i in range(len(gameData['recoveryProofs'])):
        new_element = dict(zip(keys, gameData['recoveryProofs'][i]))
        gameData['recoveryProofs'][i] = new_element
        
    # change the big decimal numbers as a hex-string 
    # in the nested dictionary except for the key 't'
    for key in gameData:

        if key == 'T':
            pass
        elif key == 'setupProofs' or key == 'recoveryProofs':
            for i in range(len(gameData[key])):
                for innerKey in gameData[key][i]:
                    if innerKey != 'T':
                        gameData[key][i][innerKey] = decimal_to_padded_hex(gameData[key][i][innerKey])
                        
        elif key == 'randomList' or key == 'commitList':
            for i in range(len(gameData[key])):
                gameData[key][i] = decimal_to_padded_hex(gameData[key][i])
                
        else: # key == 'n' or key == 'x' or key == 'y' or key == 'v':
            gameData[key] = decimal_to_padded_hex(gameData[key])
        
    encoded_data = ''.join(NoQuoteEncoder().iterencode(gameData))
    
    # 1. print data on terminal
    print('\n\n\n[+] Game Data: ', encoded_data)#json.dumps(gameData, indent=2))

    # 2. print data as a JSON-like file
    #custom_json_string = ", ".join(f"{key}: \"{value}\"" for key, value in gameData.items())
    #custom_json_string = f"{{ {custom_json_string} }}"
    
    # Format the current time as YYYYMMDD_HHMMSS
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"./testlog/data_{current_time}.json"

    # Writing the data to a JSON file
    with open(file_name, 'w') as file:
        file.write(encoded_data)
    
    print(f'[+] Game Data is saved as {file_name}')