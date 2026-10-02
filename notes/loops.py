#for loops
import time
# Iteration
siblings = ["ryker", "golden"]
for sibling in siblings:
    print(f"good morning {sibling}!")



grades = [100, 87, 53, 45, 78, 72, 88, 3, 94]
average = 0
for grade in grades:
    average += grade
    print(f"{grade} was added.")

average = average/len(grades)
print(f"the average grade is {average:.2f}")

for i in range(20,0,-1):
    print(i)
    time.sleep(0.5)


for i in range(20,21,2):
    print(i)
    time.sleep(0.5)
    if i == 12:
        print("wait it is lunch time")
        break