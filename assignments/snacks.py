import random

snack_price = random.randint(1,100000)
total_inserted = 0.00

print(f"welcome to the vending machine! snacks cost ${float(snack_price):.2f}")
discount = snack_price / 20000 + 1
print(f"but for you we will make it just {float(discount):.2f}")