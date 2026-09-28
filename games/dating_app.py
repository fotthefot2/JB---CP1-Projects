people = {
    "juliet": 30,
    "anna": 20,
    "po": 30,
    "laura": 63,
    "paul": 25,
    "cory": 45,
}

range_one = int(input("What is the lowest you would date: "))
range_two = int(input("What is the highest you would date: "))

eligible_dates = []

for name, age in people.items():
  if range_one <= age <= range_two:
    eligible_dates.append(name)

if eligible_dates:
  print(
      "Based on your range, you can date:",
      ", ".join(eligible_dates).title(),
  )
else:
  print("No one matches your age range!")