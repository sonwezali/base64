# __      _____ _    ___ ___  __  __ ___   _____ ___    ___   _   ___ ___  __ _ _    ___   _____  
# \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \  | _ ) /_\ / __| __|/ /| | |  | __| / /   \ 
#  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) | | _ \/ _ \\__ \ _|/ _ \_  _| | _| / /| |) |
#   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  |___/_/ \_\___/___\___/ |_|  |___/_/ |___/ 


# This is a Base64 encoder/decoder written by sonwezali using Python.

def main():
    mode = get_input()
    if (mode == "E"):
        encode("test")
    else:
        decode("test")

def get_input():
    mode = ""
    while(mode not in ["E", "D"]):
        mode = input('"E" to encode, "D" to decode: ').upper()
    return mode

def encode(input_value):
    print("entered to encode " + input_value)

def decode(input_value):
    print("entered to decode " + input_value)

main()
