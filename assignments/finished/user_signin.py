# Judah Beagley, period 1, user sign in

#correct inputs
correct_user_name = "coolperson"
correct_password = "123abc"

#loop for inputs
while True:
    user_name = input ("ENTER USER: ")
    password = input("ENTER PASSWORD: ")
    if user_name == correct_user_name: #checks first for correct user
        if password == correct_password: #then checks for correct password
            break #only breaks if both are correct
        else:
            print("incorrect username and/or password")
    else:
        print("incorrect username and/or password")

print("logged in")