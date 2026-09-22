#Judah Beagley, period 1, crew share

import random

total_units = random.randint(500,5000)

while True:
    try:
        crew = int(input("how many pirates be on board matie: "))
        break
    except:
        print("thats not a valid number")
pirates = crew + 2

#this next variable is to make my other variables make more sense
quick_cash = crew * 3
keeping_units = total_units - quick_cash

yondu_share = round(keeping_units * 0.13,2)
first_cut = round(keeping_units * 0.87,2)
peter_share = round(first_cut * 0.11,2)
second_cut = round(first_cut * 0.89,2)
crew_share = round(second_cut / pirates,2)

yondu_share = round(yondu_share + crew_share,2)
peter_share = round(peter_share + crew_share,2)

print(f"total units scavenged: {total_units}")
print(f"what Yondu got: {yondu_share}")
print(f"what Peter got: {peter_share}")
print(f"what the crew got: {crew_share}")