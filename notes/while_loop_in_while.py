problem = False
repeat = 11
print("you have 10 tries to figure out the problem")
while True:
    
    repeat -= 1
    while repeat > 0 and True:
        print(f"{repeat} tries left")
        problem = input("what is 12 x 12? ")
        if problem is not 144:
            print("incorrect")
            break
        elif problem == 144:
            print("correct!")
            problem = True
            break
    if problem == True:
        break