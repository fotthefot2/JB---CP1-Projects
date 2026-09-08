"""full_name = input("full name: ")

print(f"hello {full_name} welcome to my program!")"""

letter = input("give me a letter: ")
letter = letter[0].lower()
number_value = ord(letter)
print(number_value)
number_value +=2
new_letter = chr(number_value)
print(f"your letter was {letter} now it is {new_letter}")