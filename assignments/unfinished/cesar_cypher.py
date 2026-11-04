# judah beagley, period 1, Caesar cypher

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def encode (code, shift):
    letters = list(code.lower())
    new_letters = []

    for letter in letters:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift) % 26
            new_letters.append(alphabet[new_index])
        else:
            new_letters.append(letter)

    return "".join(new_letters) #THIS FUNCTION TOOK ME SO LONG TO FIGURE OUT I NEVER WANT TO DO THIS AGAIN

    

print("welcome to the Caesar Cypher.")
while True:

    option = input("do you want to encode or decode? ")
    if option == "encode":
        code = input("enter the message you want to encode: ")
        while True:
            try:
                shift = int(input("how much do you want to shift it? (EX: 2) "))
            except ValueError:
                print("INVALID INPUT")
            else:
                result = encode(code, shift)
                print(f"your encoded message is {result}")
                break

    elif option == "decode":
        code = input("what is the message you want to decode: ")
        print("here are all the possible combinations:")
        print(code)
        break
    break
print("if you see this print statement, it all hopefully works")