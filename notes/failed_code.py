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