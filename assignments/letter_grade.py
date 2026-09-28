#judah beagley, period 1,
while True:
    try:
        grade = float(input("what is your grade: "))
        break
    except ValueError:
        print("that is not a valid grade")
if grade <=93>=100:
    print("you have an A")
elif grade <=90>=92:
    print("you have an A-")
elif grade <=87>=89:
    print("you have a B+")
elif grade <=83>=86:
    print("you have a B")
elif grade <=80>=82:
    print("you have a B-")
elif grade <=77>=79:
    print("you have a c+")
elif grade <=73>=76:
    print("you have a c")
elif grade <=70>=72:
    print("you have a c-")