#judah beagley, period 1, password strength checker
character = False

print("welcome to the most amazing password strength checker ever! Even in one million billion years, never will another one come close to how good th== one is.")


while True:
    password = input("enter password: ")
    password_list = list(password)
    if len(password) < 8:
        character = True
    if any(character.isupper() for character in password_list):
        uppers = False
    else:
        uppers = True
    if any(character.islower() for character in password_list):
        lowers = False
    else:
        lowers = True
    if any(character.isnumeric() for character in password_list):
        numbers = False
    else:
        numbers = True
    if any(not character.isalum() for character in password_list):
        special_chars = False
    else:
        special_chars = True
    #i know i could have made this next part better, and i know how to, but i was already too far in, and it's more personal.
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
    elif character == False and lowers == False and special_chars == False and uppers == False and numbers == False:
        print ("")
        break
    elif character == False and lowers == False and special_chars == False and uppers == True and numbers == True:
        print ("password is missing at least one capital letter and one number. medium")
        break
    elif character == False and lowers == False and special_chars == False and uppers == False and numbers == False:
        print ("wow, im stealing that one. very strong")
        break
