#judah beagley, period 1, turtle race
import random as r
import turtle as t
import time


turtle_green = t.Turtle()
turtle_blue = t.Turtle()
turtle_red = t.Turtle()
turtle_yellow = t.Turtle()
turtle_purple = t.Turtle()
finish_line = t.Turtle()

turtle_green.color("green")
turtle_blue.color("blue")
turtle_red.color("red")
turtle_yellow.color("yellow")
turtle_purple.color("purple")
finish_line.hideturtle()
finish_line.up()
turtle_yellow.up()
turtle_red.up()
turtle_purple.up()
turtle_green.up()
turtle_blue.up()
finish_line.goto(200,60)
finish_line.down()
finish_line.goto(200,-60)
finish_line.goto(220,-60)
finish_line.goto(220,60)
finish_line.goto(200,60)

bet = input("the race is about to start. What turtle will you bet on: green, blue, red, purple, or yellow. purple starts behind the rest. type one of thoses in: ")

turtle_green.goto(00,20)
turtle_blue.goto(00,40)
turtle_red.goto(00,-20)
turtle_yellow.goto(00,-40)
turtle_purple.goto(-50,0)
print("the race will start in")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("GOOOOOO!")

while True:
    numbers = r.randint(10, 21)
    movement = int(numbers)
    choice = r.choice([turtle_yellow, turtle_blue, turtle_green, turtle_purple, turtle_purple, turtle_yellow, turtle_blue, turtle_green, turtle_red, turtle_purple])
    
    if choice == turtle_yellow:
        if movement < 15:
            turtle_yellow.forward(movement*2)
        else:
            turtle_yellow.forward(movement)
        time.sleep(0.01)  
        if turtle_yellow.xcor() >= 200:
            print("yellow wins!")
            if bet == "yellow" or bet == "yellow turtle":
                print("you won your bet!")
                time.sleep(3)
                break
            else:
                print("sadly that wasn't your bet")
                time.sleep(3)
                break  

    elif choice == turtle_red:
        turtle_red.forward(movement*3)
        time.sleep(0.5)
        if turtle_red.xcor() >= 200:
            print("red wins!")
            if bet == "red" or bet == "red turtle":
                print("you won your bet!")
                time.sleep(3)
                break
            else:
                print("sadly that wasn't your bet")
                time.sleep(3)
                break
            

    elif choice == turtle_green:
        if movement >= 20:
            turtle_green.forward(movement*5)
        else:
            turtle_green.forward(movement*.75)
        time.sleep(0.01)
        if turtle_green.xcor() >= 200:
            print("green wins!")
            if bet == "green" or bet == "green turtle":
                print("you won your bet!")
                time.sleep(3)
                break
            else:
                print("sadly that wasn't your bet")
                time.sleep(3)
                break
            

    elif choice == turtle_blue:
        turtle_blue.forward(movement*.5)
        racers = [turtle_green, turtle_purple, turtle_red, turtle_yellow]
        leader = max(racers, key=lambda turtle: turtle.xcor())
        leader.backward(movement*5)

        time.sleep(0.01)
        if turtle_blue.xcor() >= 200:
            print("blue turtle won!")
            if bet == "blue" or bet == "blue turtle":
                print("you won your bet!")
                time.sleep(3)
                break
            else:
                print("sadly that wasn't your bet")
                time.sleep(3)
                break
    elif choice == turtle_purple:
            turtle_purple.forward(movement)
            time.sleep(0.01)
            if turtle_purple.xcor() >= 200:
                print("purple turtle won!")
                if bet == "purple" or bet == "purple turtle":
                    print("you won your bet!")
                    time.sleep(3)
                    break
                else:
                    print("sadly that wasn't your bet")
                    time.sleep(3)
                    break
#i should have read the requirements before coding this. Sorry there is no functions.