#judah beagley, period 1, combat program
import time
import random

def qte(time_limit=0.4):
    print("get ready to dodge the next attack by pressing enter on the next message...")
    time.sleep(random.uniform(1.5,4.0)) #gives a random delay before the qte

    start_time = time.time()
    input("press enter!")
    end_time = time.time()

    reaction_time = end_time - start_time

    if reaction_time <= time_limit:
        print("You dodged their attack!")
        return False
    else:
        print("you got hit!")
        return True #why does it only do it sometimes

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
        hp = 50
        break
    elif chosen_class == "2":
        character = "mage"
        print("you've chosen mage!")
        hp = 25
        break
    elif chosen_class == "3":
        character = "archer"
        print("you've chosen archer!")
        hp = 35
        break
    else:
        print("invalid answer try again")
print(chosen)
while True:
    enemy_hp = 50
    print("this is the last fight you will need to do before the world is free from tyrany.")
    print("before you stands the strongest creature you have ever fought; his skin tightly packed around every well defined muscle. He eyes you with murderous intent; it is time to fight.")
    input("PRESS ENTER TO START THE BATTLE: ")
    while True:
        damage = random.randrange(3,13)
        roll = random.randrange(1,11)
        if qte(time_limit=0.4) is True:
            if roll == 5:
                print("it was a critical hit!")
                print(f"you take {damage*2} damage!")
                hp = hp - damage*2
            else:
                print(f"you take {damage} damage!")
                hp = hp - damage
        if hp <=0:
            print("you died.")
            win = False
            break
        print(f"you have {hp} hp left")
        while True:
            print("its your turn now.")
            print("CHOICES:")
            print("1  attack")
            print("2  heal 1-5 hp")
            while True:
                choice = input("what will you do?")
                if choice is "1":
                    if character is "fighter":
                        attack_dice = random.randrange(3,18)
                        second_attack = ()
                    elif character is "mage":
                        attack_dice = random.randrange(1,11)
                        second_attack = random.randrange(1,11)
                    elif character is "archer":
                        attack_dice = random.randrange(5,13)
                        second_attack = random.randrange(2,5)
                    total_damage = attack_dice + second_attack
                    to_hit = random.randrange(6,26)
                    if to_hit <= 14:
                        print("you hit them!")
                        print(f"they take {total_damage}")
                        enemy_hp = enemy_hp = total_damage
                    else:
                        print("you missed")
                    input("press enter to continue")
                    break