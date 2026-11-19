# judah beagley, period 1, order up
import time
def clean(**kwargs):
    if not kwargs.get("data"):
        return "there is nothing"
    elif kwargs.get("data"):
        if kwargs.get("type") == "str":
            return kwargs["data"].strip().lower()
        elif kwargs.get("type") == "int":
            return int(kwargs['data'])
        elif kwargs.get("type") == "float":
            if kwargs.get("decimals"):
                decimals = kwargs.get("decimals")
            return round(float(kwargs["data"]), kwargs["decimals"])
        elif kwargs.get("type") == "list":
            return str(f"{x}, " for x in kwargs["data"])
        elif kwargs.get("type") == "bool":
            return f"{kwargs['data']}"
        else:
            return "why is this not a data type..."


print("welcome to my very fancy resturant!")
time.sleep(1)
print("please, our resturant expects you to at least order a drink.")
print("here is the menu:")
time.sleep(0.5)
while True:
    try:
        user_answer = input("how many: ")
        print(clean(type="int", data=user_answer))
        break
    except ValueError:
        print("not a number")