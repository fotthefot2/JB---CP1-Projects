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

def critical(roll=random.randrange(0,11)):
    if roll >= 10:
        print("It was a critical hit!")
        return True
    else:
        return False
def class_info(stats):
    print(f"special attribute: {chosen}")
    if character == "fighter":
        stats = print("HP:50|SPEED:20|MAGIC:fire|")
    elif character == "mage":
        stats = print("HP:20|SPEED:25|MAGIC:all")
    elif character == "archer":
        stats = print("HP:35|SPEED:35|MAGIC:wind")
    return stats
chosen = random.randrange(0,11)
if chosen >= 0 and chosen <6:
    chosen = "none"
elif chosen >=5 and chosen <10:
    chosen = "flare"
elif chosen == 10:
    chosen = "the_chosen"
while True:
    print("you can choose between these three characters. enter either 1 2 or 3")
    print("1 fighter")
    print("2 mage")
    print("3 archer")
    chosen_class = input("choose: ")
    if chosen_class == "1":
        character = "fighter"
        print("you've chosen fighter!")
        break
    elif chosen_class == "2":
        character = "mage"
        print("you've chosen mage!")
        break
    elif chosen_class == "3":
        character = "archer"
        print("you've chosen archer!")
        break
    else:
        print("invalid answer try again")
print(chosen)
while True:
    break