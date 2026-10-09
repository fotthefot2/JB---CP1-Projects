#judah beagley

import random
import time
goose = random.randint(1,20)
duck = 1

while goose > duck:
    print("duck")
    time.sleep(0.1)
    duck += 1

print("GOOSE!")


count = 30

while count >= 1:
    print(count)
    time.sleep(0.1)
    count -= 1





    number = random.randint(1,101)

    while True:
        while True:
            try:
                guess = int(input("guess a number from 1 to 100: "))
                if guess < 0 or guess > 100:
                    print("read the rules...")
                    continue
                break
            except:
                print("that isn't a number")

        if guess == number:
            print("you win!")
            break
        elif guess < number:
            print("higher")
        elif guess > number:
            print("lower")
        else:
            print("you win!")
            break