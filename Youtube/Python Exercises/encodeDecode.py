alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(string): #apple, "a" ->  
    returnText = ""

    for char in string:
        if not char in alphabet:
            returnText += char
        else:
            returnText += alphabet[(alphabet.index(char)+2)%26]

    return returnText

def decode(string):
    returnText = ""

    for char in string:
        if not char in alphabet:
            returnText += char
        else:
            returnText += alphabet[(alphabet.index(char)-2)%26]

    return returnText

action = input("Would you like to encode or decode? ")
text = input("Enter your text here: ")

if action == "encode":
    print(encode(text))
elif action == "decode":
    print(decode(text))