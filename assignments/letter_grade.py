#judah beagley, period 1,
while True:
    try:
        grade = int(input("what is your grade(WHOLE NUMBERS ONLY): "))
        if grade >=0:
            break
    except ValueError:
        print("that is not a valid grade")
    else:
        print("that is not a valid grade")
if grade >=94:
    print("you have an A")
elif grade >=90 and grade <=93:
    print("you have an A-")
elif grade >=87 and grade <=89:
    print("you have a B+")
elif grade >=84 and grade <=86:
    print("you have a B")
elif grade >=80 and grade <=83:
    print("you have a B-")
elif grade >=77 and grade <=79:
    print("you have a c+")
elif grade >=74 and grade <=76:
    print("you have a c")
elif grade >=70 and grade <=73:
    print("you have a c-")
elif grade >=67 and grade <=69:
    print("you have a d+")
elif grade >=64 and grade <=66:
    print("you have a d")
elif grade >=60 and grade <=63:
    print("you have a d-")
else:
    print("you are failing and you should be ASHAMED OF YOURSELF")
