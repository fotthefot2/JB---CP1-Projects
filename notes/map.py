#judah beagley
# map: process of running a function or operations on each item in a list
def times(number):
    return number *2

numbers = range (1,6)

multiplied_numbers = map(times,numbers)

print(*list(multiplied_numbers))
new_numbers = []
for number in numbers:
    new_numbers.append(number*2)
print(*new_numbers)