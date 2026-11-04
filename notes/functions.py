#judah beagley
attempts = 0
def stupid_proof(user_answer, correct):
    user_answer = user_answer.strip().title()
    if user_answer in correct:
        return True, user_answer, attempts + 1
    else:
        return False, user_answer, attempts + 1


while True:
    capital = input("what's the capital of france? ")
    correct, capital, attempts = stupid_proof(capital, ["Oui Oui Oui Oui! It Is Paris. Merci", "Paris"])
    if correct:
        print(f"good job {capital} is correct")
        break
    else:
        print(f"try again. {capital} is not correct. you have tried {attempts} times.")