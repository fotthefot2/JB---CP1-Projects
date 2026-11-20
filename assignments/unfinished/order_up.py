#judah beagley
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
            decimals = kwargs.get("decimals", 2)
            return round(float(kwargs["data"]), decimals)
        elif kwargs.get("type") == "list":
            return ", ".join(str(x) for x in kwargs["data"])
        elif kwargs.get("type") == "bool":
            return f"{kwargs['data']}"
        else:
            return "why is this not a data type..."

# the prices are in cents btw
main = {
    "burger": 550,
    "chicken sandwich": 400,
    "chicken tenders": 600,
    "carne asada": 1200
}
sides = {
    "mac'n cheese": 200,
    "fries": 350
}
drinks = {
    "lemonade": 250,
    "soda": 200,
    "milkshake": 600
}

# put it all in one dictionary
full_menu = {
    "M A I N S": main,
    "S I D E S": sides,
    "D R I N K S": drinks
}

# what they want
order = {}

print("Welcome to my very fancy restaurant!")
time.sleep(1)
print("Please note: our restaurant expects you to order at least one drink, two sides, and one main dish.\n")
time.sleep(0.5)

# this is the reason this assignment is late btw
print("--- M E N U ---")
for category, items in full_menu.items():
    print(f"\n{category}")
    for food, price in items.items():
        # converts cents to dollars
        print(f"  {food.title()} - ${price / 100:.2f}")


while True:
    print("\nType an item to order, or type 'done' to finish.")
    raw_choice = input("What would you like? ")
    choice = clean(type="str", data=raw_choice)

    if choice == "done":
        # rule
        has_drink = any(item in drinks for item in order)
        side_count = sum(quantity_amount for item, quantity_amount in order.items() if item in sides)
        has_sides = side_count >= 2
        has_main = any(item in main for item in order)
        if not has_drink or not has_sides or not has_main:
            print("Ahem! Remember, our fancy restaurant expects you to order at least a drink, two sides and one main dish.")
            continue
        else:
            break

    # checks if the item is real
    if choice in main or choice in sides or choice in drinks:
        while True:
            try:
                quantity_question = input(f"How many {choice}s? ")
                quantity_amount = clean(type="int", data=quantity_question)
                if quantity_amount > 0:
                    # Add to order dictionary (adds to existing count if already ordered)
                    order[choice] = order.get(choice, 0) + quantity_amount
                    print(f"Added {quantity_amount}x {choice} to your order!")
                    break
                else:
                    print("You can't just order 0 of something.")
            except ValueError:
                print("Not a number!")
    else:
        print("Thats not on our menu...")

# printing the receipt
print("\n--- Y O U R   R E C E I P T ---")
# merging it all
all_prices = {**main, **sides, **drinks}
total_cents = 0

for item, quantity_amount in order.items():
    item_cost = all_prices[item] * quantity_amount
    total_cents += item_cost
    print(f"{quantity_amount}x {item.title()} - ${item_cost / 100:.2f}")

print("-------------------------------")
print(f"TOTAL: ${total_cents / 100:.2f}")