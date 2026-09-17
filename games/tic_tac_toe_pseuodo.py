# Initialize board spaces
A1 = " "
A2 = " "
A3 = " "
B1 = " "
B2 = " "
B3 = " "
C1 = " "
C2 = " "
C3 = " "


def display_board():
    print(f"1 {A1}   {B1}   {C1}")
    print(f"2 {A2}   {B2}   {C2}")
    print(f"3 {A3}   {B3}   {C3}")
    print("   A   B   C")


# Rules prompt
user_knows_rules = input("Do you know the rules? ")
rules = (
    "There is a 3x3 board and you put your piece on another empty slot on the board."
)

if user_knows_rules.lower() == "no":
    print(rules)
else:
    print("ok")

player_one = None
player_two = None


def win_question_x():
    if A1 == A2 == A3 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif B1 == B2 == B3 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif C1 == C2 == C3 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif A1 == B1 == C1 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif A2 == B2 == C2 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif A3 == B3 == C3 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif A1 == B2 == C3 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    elif A3 == B2 == C1 == "X":
        print("PLAYER 1 WINS!!!")
        return True
    return False


def win_question_o():
    if A1 == A2 == A3 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif B1 == B2 == B3 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif C1 == C2 == C3 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif A1 == B1 == C1 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif A2 == B2 == C2 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif A3 == B3 == C3 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif A1 == B2 == C3 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    elif A3 == B2 == C1 == "O":
        print("PLAYER 2 WINS!!!")
        return True
    return False


display_board()

# Main Game Loop
while True:
    # Player 1 Turn
    user_input = input("player 1 go: ")

    if user_input == "A1" and A1 == " ":
        A1 = "X"
    elif user_input == "A2" and A2 == " ":
        A2 = "X"
    elif user_input == "A3" and A3 == " ":
        A3 = "X"
    elif user_input == "B1" and B1 == " ":
        B1 = "X"
    elif user_input == "B2" and B2 == " ":
        B2 = "X"
    elif user_input == "B3" and B3 == " ":
        B3 = "X"
    elif user_input == "C1" and C1 == " ":
        C1 = "X"
    elif user_input == "C2" and C2 == " ":
        C2 = "X"
    elif user_input == "C3" and C3 == " ":
        C3 = "X"
    else:
        print("you messed up something so now you don't get to go.")

    display_board()
    if win_question_x():
        break

    # Player 2 Turn
    user_input = input("player 2 go: ")

    if user_input == "A1" and A1 == " ":
        A1 = "O"
    elif user_input == "A2" and A2 == " ":
        A2 = "O"
    elif user_input == "A3" and A3 == " ":
        A3 = "O"
    elif user_input == "B1" and B1 == " ":
        B1 = "O"
    elif user_input == "B2" and B2 == " ":
        B2 = "O"
    elif user_input == "B3" and B3 == " ":
        B3 = "O"
    elif user_input == "C1" and C1 == " ":
        C1 = "O"
    elif user_input == "C2" and C2 == " ":
        C2 = "O"
    elif user_input == "C3" and C3 == " ":
        C3 = "O"
    else:
        print("you messed up something so now you don't get to go.")

    display_board()
    if win_question_o():
        break