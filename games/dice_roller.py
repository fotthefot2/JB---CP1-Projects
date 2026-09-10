#Judah Beagley, period 1, dice roller
import random
print("welcome to the dice roller. i hope you roll high but mostly have fun.")

dice_selection = input("what dice would you want to roll? Our selection ranges from d4, d6, d8, d10, d12, and d20. Just type the number you want and its yours to roll: ")

if dice_selection == "4":
    dice_selection = random.randint(1,4)
elif dice_selection == "6":
    dice_selection = random.randint(1,6)
elif dice_selection == "8":
    dice_selection = random.randint(1,8)
elif dice_selection == "10":
    dice_selection = random.randint(1,10)
elif dice_selection == "12":
    dice_selection = random.randint(1,12)
elif dice_selection == "20":
    dice_selection = random.randint(1,20)
elif dice_selection == "lucky4":
    dice_selection = random.randint(3,4)
elif dice_selection == "lucky6":
    dice_selection = random.randint(3,6)
elif dice_selection == "lucky8":
    dice_selection = random.randint(5,8)
elif dice_selection == "lucky10":
    dice_selection = random.randint(6,10)
elif dice_selection == "lucky12":
    dice_selection = random.randint(5,12)
elif dice_selection == "lucky20":
    dice_selection = random.randint(11,20)
else:
    dice_selection = ("nothing you didn't type one of the inputs try again")

print(f"you rolled {dice_selection}!")