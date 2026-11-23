#judah beagley, period 1, flexible calculator
import math
def clean(**kwargs):
    if not kwargs.get("data"):
        return "there is nothing"
    elif kwargs.get("data"):
        if kwargs.get("type") == "str":
            return kwargs["data"].strip().lower()
        elif kwargs.get("type") == "int":
            return int(kwargs['data'])
        elif kwargs.get("type") == "float":
            decimals = kwargs.get("decimals", 2)
            return round(float(kwargs["data"]), decimals)
        elif kwargs.get("type") == "list":
            return ", ".join(str(x) for x in kwargs["data"])
        elif kwargs.get("type") == "bool":
            return f"{kwargs['data']}"
        else:
            return "why is this not a data type..."
def sum():
    print()
def average():
    print()
def max():
    print()
def min():
    print()
def product():
    print()

print("welcome to the calculator.")
while True:
    calc = print("here are the options:\n1 sum calculator\n2 average calculator\n3 max calculator\n4 min calculator\n5 product calculator\n6 exit\nType the number please")
    if calc == "1":
        sum()
    elif calc == "2":
        average()
    elif calc == "3":
        max()
    elif calc == "4":
        min()
    elif calc == "5":
        product()  
    elif calc == "6":
        break