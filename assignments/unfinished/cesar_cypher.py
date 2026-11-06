# judah beagley, period 1, Caesar cypher
def encode(code, shift):
    new_letters = []# puts it all in a place i can append it and change it and manipulate it easier
    for letter in code:
        if letter .isalpha():
            start = ord("A") if letter.isupper() else ord("a") #puts it all on the same line so that it can remain a single variable
            new_code = start + (ord(letter) - start + shift) % 26 # THIS WAS SO ANNOYING TO MAKE THIS SINGLE LINE OF CODE. i had to use this math to get what i wanted.
            new_letters.append(chr(new_code)) 
        else:
            new_letters.append(letter)

    return "".join(new_letters)

def decode(code, shift):
    new_letters = []
    for letter in code:
        if letter.isalpha():
            characters = ord("A") if letter.isupper() else ord("a")
            new_code = characters + (ord(letter) - characters - shift) % 26 
            new_letters.append(chr(new_code)) 
        else:
            new_letters.append(letter)

    return "".join(new_letters)



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
print("Thank you for using my Caesar Cypher.")