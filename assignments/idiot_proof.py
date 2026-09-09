#Judah Beagley, idiot proof assignment

# name inputs

first_name = input("What is your first name: ").strip().split()
last_name = input("What is your last name: ").strip().split()


#phone number input and checker to see if user has phone number
while True:
    try:       
        phone_number = int(input("What is your phone number? if you dont have a number type 0: ").strip())

        break
    except ValueError:
        print("What is not a valid phone number")
if phone_number == ("0"):
    phone_number = False

while True:
    try:
        gpa = float(input("What is your GPA: "))
        if 0 <= gpa <= 5:
            break
        else:
            print("that is not a valid GPA")
    except ValueError:
        print("that is not a valid GPA")

if phone_number == False:
    print(f"Name= {first_name} {last_name}")
    print(f"you have no phone number")
    print(f"GPA= {gpa}")
else:
    print(f"Name= {first_name} {last_name}")
    print(f"phone number= {phone_number}")
    print(f"GPA= {gpa}")