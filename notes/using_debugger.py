
scores = [12, 45, 7, 68, 33, 90, 21]

running_total =0
highest_score = 0

for score in scores:
    running_total += score
    if score > highest_score:
        highest_score = score

print(f"total: {running_total}")
print(f"highest score: {highest_score}")