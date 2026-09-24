#judah beagley, conditionals
drive = ()
icecream = input("can i get icecream? ")

if icecream == ("no"):
    icecream = False
if icecream == ("yes"):
    icecream = True
if icecream == True:
    drive = input("can you drive me? ")
elif drive == ("no"):
    drive = False
    icecream == False
elif drive == ("yes"):
    drive = True
grade = int(input("pick a random number from 1-100 for no reason at all: "))
if grade >= 70:
    print("you are passing yay for you")
else:
    print("what the helly?")
    print("why aren't you passing bud?")
    print("maybe retake that quiz.")

    while icecream == False:
        print("why")
        print("would")
        print("you")
        print("say")
        print("no")

    username = input("what is your username bud: ")

    if bool(username):
        print("you didnt type it in budd")
    elif username == "LaRose":
        print("you are the alpha")
    else:
        print("you are a student!")

    raining = False

    if raining:
        print("bring an umbrella hahahahaha")
    else:
        print("wear sunscreen")

