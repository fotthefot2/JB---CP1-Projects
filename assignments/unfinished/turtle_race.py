#judah beagley, period 1, turtle race
import random as r
import turtle as t
import time
turtle_green = t.Turtle()
turtle_blue = t.Turtle()
turtle_red = t.Turtle()
turtle_yellow = t.Turtle()

turtle_green.color("green")
turtle_blue.color("blue")
turtle_red.color("red")
turtle_yellow.color("yellow")

bet = input("the race is about to start. What turtle will you bet on: green, blue, red and yellow. type one of thoses in: ")
turtle_green.goto(00,20)
turtle_blue.goto(00,40)
turtle_red.goto(00,-20)
turtle_yellow.goto(00,-40)
print("the race will start in")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GOOOOOO!")

while True:
    numbers = r.randint(10, 20)  # adjusted step size so they don't teleport instantly
    movement = int(numbers)
    choice = r.choice([turtle_yellow, turtle_blue, turtle_green, turtle_red])  # fixed syntax: () around []
    
    if choice == turtle_yellow:
        turtle_yellow.forward(movement)  # changed right() to forward() so it moves across x-axis
        time.sleep(0.1)  # small pause so you can see the steps
        if turtle_yellow.xcor() >= 100:
            print("yellow wins!")
            if bet == "yellow" or bet == "yellow turtle":
                print("you won your bet!")
                break
            else:
                print("sadly that wasn't your bet")
                break  

    elif choice == turtle_red:
        turtle_red.forward(movement)
        time.sleep(0.1)
        if turtle_red.xcor() >= 100:
            print("red wins!")
            if bet == "red" or bet == "red turtle":
                print("you won your bet!")
                break
            else:
                print("sadly that wasn't your bet")
                break
            

    elif choice == turtle_green:
        turtle_green.forward(movement)
        time.sleep(0.1)
        if turtle_green.xcor() >= 100:
            print("green wins!")
            if bet == "green" or bet == "green turtle":
                print("you won your bet!")
                break
            else:
                print("sadly that wasn't your bet")
                break
            

    elif choice == turtle_blue:
        turtle_blue.forward(movement)
        time.sleep(0.1)
        if turtle_blue.xcor() >= 100:
            print("blue turtle won!")
            if bet == "blue" or bet == "blue turtle":
                print("you won your bet!")
                break
            else:
                print("sadly that wasn't your bet")
                break
