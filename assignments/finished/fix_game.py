#judah beagley, period 1, fix the game

import random

scores = []
rounds = 3

print("Welcome to Guess the Number! You'll play 3 rounds.")
print("Each round, try to guess the number in as few tries as possible.\n")

for round_num in range(1, rounds + 1):
    secret_number = random.randint(1, 20)
    guesses = 0
    found = False

    print(f"--- Round {round_num} ---")

    while found == False: #stynax error
        guess = int(input("Guess a number between 1 and 20: "))
        guesses = guesses + 1

        if guess == secret_number:
            print(f"Correct! It took you {guesses} guesses.")
            found = True
        elif guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")

    scores.append(guesses)

print("\n--- Game Over ---")
print("Your guesses per round: " ,scores) #switched to comma to fix syntax error

total = 0
for score in scores:
    #logic error
    total = total + score

average = total / rounds
average = round(average,2)
print("Your average guesses per round was "  ,(average))

best_round = scores[0]
for i in range(0, rounds): #uneeded -1 runtime error and 0, not 1. logic error
    if scores[i] < best_round:
        best_round = scores[i]

print(f"Your best round took only {best_round} guesses!")