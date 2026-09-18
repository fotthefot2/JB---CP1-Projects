#Judah Beagley, period 1, crew share

import random

total_units = random.randint(500,5000)

while True:
    try:
        pirates = int(input("how many pirates be on board matie: "))
    except:
        print("thats not a valid number")
    else:
        if pirates >= 2:
            break
        else:
            print("dont forget about Yondu and Peter. (you need at least 2)")
