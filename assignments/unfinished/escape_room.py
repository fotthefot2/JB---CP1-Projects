#Judah Beagley, period 1, escape room
import random
import time
print("you wake up in a mysterious place. It seems to be a dark room with white tiles on the ground and silky, almost moist walls with the same tile look. You remember the last time you were awake. You were walking down the street at night, coming back from the gas station right by your house when a cloth was put over your mouth and nose. the next thing you knew you were in here. You see on your left a box with a small drop down for items to come into. Sort of like a vending machine. And to your right you see the way out as well as a passcode. You realize you were put in an escape room. Above the code you see a number. The number reads five.")
print()
hints = ['The code is about a specific holiday.', 'The code is something celebrated with gifts', 'The code is a certain date', 'The code is something usually in this format: mm/dd']
code = 1224
attempts = 5
win = ()
time.sleep(3)
while True:
    choose = input("you figure you should try to guess a code to start. There isn't any items of interest that arent in that box to the left of you. Choose one. look around/try the code: ")
    if choose == "look around":
        d20 = random.randrange(1,21)
        print("rolling a d20")
        time.sleep(1)
        print(f"{d20}!")
        if d20 >=15 and d20 <20:
            print("you see a wire attatched to the box and the passcode. you can infer that when you input a number into the code, it lets out an item at random from the box into the area where you can pick it up. you can also see how it is connectected to the number outputting five. It likely means you only have five guesses.")
            choose = "jjsm"
        elif d20 >=10 and d20 <15:
            print("you can see the code is likely attatched to the number in some way. Perhaps through attemps left? It seems like you have 5 tries to get this right.")
            choose = "jjsm"
        elif d20 >=2 and d20 <10:
            print("you see nothing out of the ordinary, other than what you already saw. The tiles on the floor and walls look pretty cool though.")
            choose = "jjsm"
        elif d20 >= 1 and d20 <2:
            print("you actually are so blind you forget what you saw earlier. You also fall over and hit the codelock and it inputs a random code. The number goes down to four.")
            attempts = attempts-1
            choose = "jjsm"
    elif choose == "try the code" or choose == "jjsm":
        while True:
            try:
                guess = input("ENTER GUESS(4 digits only. if you put more, the guess will be wrong.): ")
                if guess == 1224:
                    print("the codelock beeps green and the door opens. You escape into an empty warehouse, and outside there is a man with a briefcase of money. He hands it to you, congragulates you, and then he knocks you out. You wake up back at the gas station with all the stuff you bought earlier on the street. You get up, and walk home. A monster in one hand, $100,000 in the other.")
                    win = "yes"
                    break
                else:
                    print("a big red error pops up on the codelock and the number above the codelock goes down one.")
                    attempts = attempts-1
                    if attempts == 0:
                        print("the number on the lock hits zero, and every thing shuts down on the strange room. A gas fills in to the room, and at first, you feel nothing, but after a while you realize how unfocused you are on everyting. A few seconds later you black out.")
                        win = "no"
                        break
                    print("you see the box on the left drop something down. You pick it up. it reads the following:")
                    hint = ()
                    print(*hint)

            except ValueError:
                print("you try your best to input that into the codelock, but you find it's just a codelock and you can't input those values in.")
    else:
        print("look at the options you have again...")