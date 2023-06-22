# __      _____ _    ___ ___  __  __ ___   _____ ___    ___   _   ___ ___  __ _ _    ___   _____  
# \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \  | _ ) /_\ / __| __|/ /| | |  | __| / /   \ 
#  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) | | _ \/ _ \\__ \ _|/ _ \_  _| | _| / /| |) |
#   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  |___/_/ \_\___/___\___/ |_|  |___/_/ |___/ 


# This is a Base64 encoder/decoder written by sonwezali.

import math

base64_values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                 "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                 "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
                 "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                 "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2",
                 "3", "4", "5", "6", "7", "8", "9", "+", "/"]

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
        group_in_six = []
        for i in range(0, 24, 6):
            six_group = twenty_four_bits[i:i+6]
            group_in_six.append(six_group)
        six_bit_groups.append(group_in_six)
    return six_bit_groups

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
            while len(binary_string_of_group) < 24:
                binary_string_of_group += "0"
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
    return groups

def group_of_binary(group):
    binary_group = []
    for quart in group:
        quart_in_bin = ""
        for ch in quart:
           value = base64_values.index(ch)
           bin_value = bin(value)[2:]
           while len(bin_value) < 6:
               bin_value = "0" + bin_value
           quart_in_bin += bin_value
        binary_group.append(quart_in_bin)
    
    return binary_group

def group_in_bytes(binary_group):
    byte_group = []
    binary_string = "".join(binary_group)

    for i in range(0,len(binary_string), 8):
        byte_group.append(binary_string[i:i+8])

    return byte_group

# function which encodes the input
def encode(input_value):
    groups = group_in_threes(input_value)
    binary_group = ascii_values_to_binary(groups) 
    six_bit_groups = grouping_in_six_bits(binary_group)
    number_of_gaps = 0
    if len(input_value) % 3 != 0:
        if len(input_value) % 3 == 1:
            number_of_gaps = 2
        else:
            number_of_gaps = 1
    for i in range(number_of_gaps):
        six_bit_groups[-1].pop()
    
    encoded_text = ""
    for quart in six_bit_groups:
        for value in quart:
            encoded_text += str(base64_values[int(value, 2)])
    
    for i in range(number_of_gaps):
        encoded_text += "="

    print('\nThe encoded text: ' + encoded_text + '\n')

# function which decodes the input
def decode(input_value):
    group = group_in_fours(input_value)
    number_of_gaps = 0
    
    while group[-1][-1] == "=":
        group[-1] = group[-1][:-1]
        number_of_gaps += 1

    binary_group = group_of_binary(group)

    if number_of_gaps == 1:
        binary_group[-1] = binary_group[-1][:16]
    elif number_of_gaps == 2:
        binary_group[-1] = binary_group[-1][:8]

    byte_group = group_in_bytes(binary_group)

    decoded_text = ""
    for byte in byte_group:
        decoded_text += chr(int(byte, 2))

    print('\nThe decoded text: ' + decoded_text + '\n')
    
main()

