#judah beagley, period 1, combat program
import time
import random

def qte(time_limit=0.5):
    print("get ready to dodge the next attack by pressing enter on the next message...")
    time.sleep(random.uniform(1.5,4.0)) #gives a random delay before the qte

    start_time = time.time()
    input("press enter!")
    end_time = time.time()

    reaction_time = end_time - start_time

    if reaction_time <= time_limit:
        print("You dodged their attack!")
        return True
    else:
        print("you got hit!")
        return False

def critical(roll=random.randint(0,11)):
    if roll >= 10:
        print("It was a critical hit!")
        return True
    else:
        return False
while True:
    print("you can choose between these three characters. enter either 1 2 or 3")
    print("1 fighter")
    print("2 mage")
    print("3 archer")
    chosen_class = input("choose: ")
    if chosen_class == 1:
        fighter = True
        break
    elif chosen_class == 2:
        mage = True
        break
    elif chosen_class == 3:
        archer = True
        break
    else:
        print("invalid answer try again")