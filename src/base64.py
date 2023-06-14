# __      _____ _    ___ ___  __  __ ___   _____ ___    ___   _   ___ ___  __ _ _    ___   _____  
# \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \  | _ ) /_\ / __| __|/ /| | |  | __| / /   \ 
#  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) | | _ \/ _ \\__ \ _|/ _ \_  _| | _| / /| |) |
#   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  |___/_/ \_\___/___\___/ |_|  |___/_/ |___/ 


# This is a Base64 encoder/decoder written by sonwezali.

import math

# main function
def main():
    print("""
           ------------------------------
          |                              |
          |    BASE64 ENCODER/DECODER    |
          |                              |
           ------------------------------
          
          """)
    mode = get_mode() # encode or decode
    if (mode == "E"): # if encode
        encode(get_input_value())
    else: # else (decode)
        decode(get_input_value())

# function to get the expression which will be encoded or decoded
def get_input_value():
    input_value = ""
    while (len(input_value) == 0):
        input_value = input("Enter the expression you want to encode/decode: ")
    return input_value

# function to define which operation to perform
def get_mode():
    mode = ""
    while (mode not in ["E", "D"]):
        mode = input('"E" to encode, "D" to decode: ').upper()
    return mode

# function to group the characters in threes wihle encoding 
def group_in_threes(expr):
    groups = []
    for i in range(math.ceil(len(expr) / 3)):
    # math.ceil() method is necessary to avoid from errors originating from
    # the cases when the length of the expr is not a product of 3. 
        start_i = 3 * i
        end_i = start_i + 3
        groups.append(expr[start_i:end_i])
    return groups

def grouping_in_six_bits(binary_groups):
    six_bit_groups = []
    for twenty_four_bits in binary_groups:
        pass

# function to convert ASCII values into binary values
def ascii_values_to_binary(groups):
    binary_groups = [] 
    if len(groups) != 0:
        for group in groups:
            binary_string_of_group = ""
            for char in group:
                len_of_binary_format = len(bin(ord(char))[2:])
                binary_string = ("0" * (8 - len_of_binary_format)) + bin(ord(char))[2:] 
                binary_string_of_group += binary_string
            binary_groups.append(binary_string_of_group)
    return binary_groups

# function to group characters in fours while decoding
def group_in_fours(expr):
    groups = []
    for i in range(math.ceil(len(expr) / 4)):
    # math.ceil() method is necessary to avoid from errors originating from
    # the cases when the length of the expr is not a product of 4. 
        start_i = 4 * i
        end_i = start_i + 4
        groups.append(expr[start_i:end_i])
    while (len(groups[-1]) < 4):
        groups[-1] += "="
    return groups

# function which encodes the input
def encode(input_value):
    print("entered to encode " + input_value)
    groups = group_in_threes(input_value)
    print(ascii_values_to_binary(groups)) 

# function which decodes the input
def decode(input_value):
    print("entered to decode " + input_value)
    print(group_in_fours(input_value))

main()

