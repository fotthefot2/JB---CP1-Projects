#judah beagley, period one, factorial calculator
import math
mathing = math.factorial
while True:
    breaker = input("do you want the code to stop(press enter if no type yes if yes): ")
    if breaker == "yes":
        break
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
        factors = range(factorial,0,-1)
        print(*factors)
        factor_map = map(mathing,factors)
        print(*list(factor_map))
    else:
        print("0 = 1")