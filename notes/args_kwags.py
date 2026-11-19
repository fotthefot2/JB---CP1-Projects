#judah beagley
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

print(clean(type="float", data="3.1415", decimals=3))
print(clean(data="utah",type = "str"))