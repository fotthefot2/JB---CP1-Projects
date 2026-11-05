"""
    if character == True and uppers == False and lowers == False and special_chars == False and numbers == False:
        print ("password is missing at least 8 characters. strong")
        break
    elif uppers == True and lowers == False and special_chars == False and character == False and numbers == False:
        print ("password is missing at least one capital letter. strong")
        break
    elif numbers == True and lowers == False and special_chars == False and character == False and uppers == False:
        print ("password is missing at least one number. strong")
        break
    elif character == False and lowers == True and special_chars == False and uppers == False and numbers == False:
        print ("password has no lowercase letters. strong")
        break
    elif character == False and lowers == False and special_chars == True and uppers == False and numbers == False:
        print ("password is missing at least one special character. strong")
        break
    elif character == True and lowers == False and special_chars == False and uppers == True and numbers == False:
        print ("password is missing at least 8 character and one capital letter. medium")
        break
    elif character == True and lowers == False and special_chars == False and uppers == False and numbers == True:
        print ("password is missing at least 8 character and one number. medium")
        break
    elif character == True and lowers == False and special_chars == False and uppers == True and numbers == True:
        print ("password is missing at least 8 character, one capital letter, and one number. weak")
        break
    elif character == True and lowers == True and special_chars == True and uppers == False and numbers == False:
        print ("password is missing at least one character, lowercase, and one special character. weak")
        break
    elif character == True and lowers == True and special_chars == False and uppers == True and numbers == False:
        print ("")
        break
    elif character == False and lowers == False and special_chars == False and uppers == True and numbers == True:
        print ("password is missing at least one capital letter and one number. medium")
        break
    elif character == False and lowers == False and special_chars == False and uppers == False and numbers == False:
        print ("wow, im stealing that one. very strong")
        break
    """
"""
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# function for the logic of encoding
def encode (code, shift):
    letters = list(code)
    new_letters = []

    for letter in letters:
        if letter in alphabet: # i had to figure out how to make it only use letters not numbers and symbols
            index = alphabet.index(letter)
            new_index = (index + shift) % 26 #the + makes it an encoder
            new_letters.append(alphabet[new_index])
        else:
            new_letters.append(letter)

    return "".join(new_letters) #THIS FUNCTION TOOK ME SO LONG TO FIGURE OUT I NEVER WANT TO DO THIS AGAIN

def decode (code, shift):
    letters = list(code)
    new_letters = []

    for letter in letters:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % 26 # the - makes it a decoder
            new_letters.append(alphabet[new_index])
        else:
            new_letters.append(letter)

    return "".join(new_letters) #this specific part took a while to get to

print("welcome to the Caesar Cypher.")
while True:

    option = input("do you want to encode or decode (or leave)? ")
    if option == "encode":
        code = input("enter the message you want to encode: ")
        while True:
            try:
                shift = int(input("how much do you want to shift it? (EX: 2) "))
            except ValueError:
                print("INVALID INPUT")
            else:
                result = encode(code, shift)
                print(f"your encoded message is: {result}")
                break

    elif option == "decode":
        code = input("what is the message you want to decode: ")
        while True:
            try:
                shift = int(input("how much do you want to shift it back? (EX: 2)"))
            except ValueError:
                print("INVALID INPUT")
            else:
                
                result = decode(code, shift)
                print(f"your decoded message says: {result}")
                break
    elif option == "leave":
        break
print("Thank you for using my Caesar Cypher.")"""
#more in the graveyard
"""
alphabet = ord()
# function for the logic of encoding
def encode (code, shift):
    letters = list(code)
    new_letters = []

    for letter in letters:
        if letter in alphabet: # i had to figure out how to make it only use letters not numbers and symbols
            index = alphabet.index(letter)
            new_index = (index + shift) % 26 #the + makes it an encoder
            new_letters.append(alphabet[new_index])
        else:
            new_letters.append(letter)

    return "".join(new_letters) #THIS FUNCTION TOOK ME SO LONG TO FIGURE OUT I NEVER WANT TO DO THIS AGAIN

def decode (code, shift):
    letters = list(code)
    new_letters = []

    for letter in letters:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift) % 26 # the - makes it a decoder
            new_letters.append(alphabet[new_index])
        else:
            new_letters.append(letter)

    return "".join(new_letters) #this specific part took a while to get to"""