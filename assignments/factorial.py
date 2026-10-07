#judah beagley, period one, factorial calculator
import math
factors = []
while True:
    try:
        factorial = int(input("what do you want the factorial of(whole numbers): "))
        if factorial >= 0:
            break
    except ValueError:
        print("invalid input")
    else:
        print("invalid input")
    
if factorial > 0:   
    factors = range(factorial,1)
    res = map(int, factors)
    print(list(res))