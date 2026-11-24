#judah beagley, period 1, flexible calculator
import math


def clean(**kwargs):
    if not kwargs.get("data"):
        return "there is nothing"
    elif kwargs.get("data"):
        if kwargs.get("type") == "str":
            return kwargs["data"].strip().lower()
        elif kwargs.get("type") == "int":
            return int(kwargs["data"])
        elif kwargs.get("type") == "float":
            decimals = kwargs.get("decimals", 2)
            return round(float(kwargs["data"]), decimals)
        elif kwargs.get("type") == "list":
            return ", ".join(str(x) for x in kwargs["data"])
        elif kwargs.get("type") == "bool":
            return f"{kwargs['data']}"
        else:
            return "why is this not a data type..."


def sum(*args):
    total = 0
    for n in args:
        total += n
    return total


def average(*args):
    if not args:
        return 0
    total = 0
    for n in args:
        total += n
    return total / len(args)


def max(*args):
    if not args:
        return None
    highest = args[0]
    for n in args[1:]:
        if n > highest:
            highest = n
    return highest


def min(*args):
    if not args:
        return None
    lowest = args[0]
    for n in args[1:]:
        if n < lowest:
            lowest = n
    return lowest


def product(*args):
    if not args:
        return 0
    result = 1
    for n in args:
        result *= n
    return result


def numbers():
    user_input = input("Enter numbers separated by spaces: ")
    cleaned_input = clean(data=user_input, type="str")
    if cleaned_input == "there is nothing":
        return []
    nums = []
    for token in cleaned_input.split():
        nums.append(clean(data=token, type="float"))
    return nums


print("welcome to the calculator.")
while True:
    choice = input(
        "here are the options:\n"
        "1 sum calculator\n"
        "2 average calculator\n"
        "3 max calculator\n"
        "4 min calculator\n"
        "5 product calculator\n"
        "6 exit\n"
        "Type the number please: "
    )
    calc = clean(data=choice, type="str")

    if calc == "1":
        nums = numbers()
        print(sum(*nums))
    elif calc == "2":
        nums = numbers()
        print(average(*nums))
    elif calc == "3":
        nums = numbers()
        print(max(*nums))
    elif calc == "4":
        nums = numbers()
        print(min(*nums))
    elif calc == "5":
        nums = numbers()
        print(product(*nums))
    elif calc == "6":
        break
    else:
        print("Invalid option.")

