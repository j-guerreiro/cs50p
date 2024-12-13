set1 = [1, 2, 3, 4, 5]
set2 = [0, 1, 3, 5, 7]

# Expected intersection = [1, 3, 5]
intersection = []

for number in set1:
    if number in set2:
        intersection.append(number)

print(intersection)