#judah beagley, period 1, password strength checker
character = False

print("welcome to the most amazing password strength checker ever! Even in one million billion years, never will another one come close to how good this one is.")


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
    if any(not character.isalnum() for character in password_list):
        special_chars = False
    else:
        special_chars = True
    break
    #i know i could have made this next part better, and i know how to, but i was already too far in, and it's more personal.
    # 1 TRUE VARIABLE (5 combinations)
while True:
    if character and lowers == False and special_chars == False and uppers == False and numbers == False:
        print("password doesn't have at least 8 characters. strong")
        break

    elif character == False and lowers == True and special_chars == False and uppers == False and numbers == False:
        print("password has no lowercase. strong")
        break

    elif character == False and lowers == False and special_chars == True and uppers == False and numbers == False:
        print("password has no special characters. strong")
        break

    elif character == False and lowers == False and special_chars == False and uppers == True and numbers == False:
        print("password has no capital letters. strong")
        break

    elif character == False and lowers == False and special_chars == False and uppers == False and numbers == True:
        print("password has no numbers. strong")
        break


    # 2 TRUE VARIABLES (10 combinations)
    elif character == True and lowers == True and special_chars == False and uppers == False and numbers == False:
        print("password doesn't have at least 8 characters and has no lowercase. medium")
        break

    elif character == True and lowers == False and special_chars == True and uppers == False and numbers == False:
        print("password doesn't have at least 8 characters and has no special characters. medium")
        break

    elif character == True and lowers == False and special_chars == False and uppers == True and numbers == False:
        print("password doesn't have at least 8 characters and has no capital letters. medium")
        break

    elif character == True and lowers == False and special_chars == False and uppers == False and numbers == True:
        print("password doesn't have at least 8 characters and has no numbers. medium")
        break

    elif character == False and lowers == True and special_chars == True and uppers == False and numbers == False:
        print("password has no lowercase and no special characters. medium")
        break

    elif character == False and lowers == True and special_chars == False and uppers == True and numbers == False:
        print("password has no lowercase and no capital letters... wait how did you do that? oh, you used only symbols and numbers. as long as you remember is ig. medium")
        break

    elif character == False and lowers == True and special_chars == False and uppers == False and numbers == True:
        print("password has no lowercase and no numbers. medium")
        break

    elif character == False and lowers == False and special_chars == True and uppers == True and numbers == False:
        print("password has no special characters and no capital letters. medium")
        break

    elif character == False and lowers == False and special_chars == True and uppers == False and numbers == True:
        print("password has no special characters and no numbers. medium")
        break

    elif character == False and lowers == False and special_chars == False and uppers == True and numbers == True:
        print("password has no capital letters and no numbers. weird password. i wouldn't guess it in a million years. but still, medium")
        break


    # 3 TRUE VARIABLES (10 combinations)
    elif character == True and lowers == True and special_chars == True and uppers == False and numbers == False:
        print("password doesn't have at least 8 characters, no lowercase, and no special characters. what a boring password. weak")
        break

    elif character == True and lowers == True and special_chars == False and uppers == True and numbers == False:
        print("password doesn't have at least 8 characters, no lowercase, and no capital letters. this password makes me cry. weak")
        break

    elif character == True and lowers == True and special_chars == False and uppers == False and numbers == True:
        print("password doesn't have at least 8 characters, no lowercase, and no numbers. you do you bro. weak")
        break

    elif character == True and lowers == False and special_chars == True and uppers == True and numbers == False:
        print("password doesn't have at least 8 characters, no special characters, and no capitals. average ahh password. weak")
        break

    elif character == True and lowers == False and special_chars == True and uppers == False and numbers == True:
        print("password doesn't have at least 8 characters, no special characters, and no numbers. just like the rest of us champ. still weak.")
        break

    elif character == True and lowers == False and special_chars == False and uppers == True and numbers == True:
        print("password doesn't have at least 8 characters, no capitals, and no numbers. understandable. weak")
        break

    elif character == False and lowers == True and special_chars == True and uppers == True and numbers == False:
        print("password has no lowercase, no special characters, and no capital letters. this isn't the phone why are you putting only numbers. weak")
        break

    elif character == False and lowers == True and special_chars == True and uppers == False and numbers == True:
        print("password has no lowercase, no special characters, and no numbers. capital letter spam. weak")
        break

    elif character == False and lowers == True and special_chars == False and uppers == True and numbers == True:
        print("password has no lowercase, no capitals, and no numbers. i have never seen such a password. weak")
        break

    elif character == False and lowers == False and special_chars == True and uppers == True and numbers == True:
        print("password has no special characters, no capital letters, and no numbers. lookin like a 5 year old made the password. weak")
        break


    # 4 TRUE VARIABLES (5 combinations)
    elif character == True and lowers == True and special_chars == True and uppers == True and numbers == False:
        print("password has numbers only. so many criteria missed its faster to say what you have. wow. very weak")
        break

    elif character == True and lowers == True and special_chars == True and uppers == False and numbers == True:
        print("password has capital letters only. so many criteria missed its faster to say what you have. wow. very weak")
        break

    elif character == True and lowers == True and special_chars == False and uppers == True and numbers == True:
        print("password has special characters only. so many criteria missed its faster to say what you have. wow. very weak")
        break

    elif character == True and lowers == False and special_chars == True and uppers == True and numbers == True:
        print("password has lowercase only. so many criteria missed its faster to say what you have. wow. very weak")
        break

    elif character == False and lowers == True and special_chars == True and uppers == True and numbers == True:
        print("password is impossible? what? how? god level password bro")
        break


    # ALL 5 TRUE
    elif character == True and lowers == True and special_chars == True and uppers == True and numbers == True:
        print("password isn't anything. doesnt work for 90 percent of apps ever. weakest password ever")
        break


    # ALL 5 FALSE
    elif character == False and lowers == False and special_chars == False and uppers == False and numbers == False:
        print("perfect. very strong")
        break