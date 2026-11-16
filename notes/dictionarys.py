# :(
budget_spending = {
    "kitchen":25,
    "outside":30,
    "bathrooms/bedrooms":15,
    "personal appliences":10,
    "garage":20
}

def ratio(spending_dictionary):
    total = sum(spending_dictionary.values())

    for category, amount in spending_dictionary.items():
        decimal_ratio = amount/total
        percentage = decimal_ratio * 100
        
budget = int(input("what is your budget?"))

avatar = {
    "water": {
        "katara": "water bender",
        "Sokka": "leader",
    },
    "earth":{
        "toph": "earth bender. THE GOATTTTTT"
    },
    "air":{
        "aang": "air bender, the avatart."

    },
    "fire":{
        "zuko": "fire bender, future fire lord",
        "iroh": "the actual goat. FIRE BENDERRR, dragon of the west",
        "azula": "fire lord for a small little bit. amazing at fire bending"
    }
}
print(avatar["fire"]["iroh"])
print(avatar.get("earth").get("toph"))