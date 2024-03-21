numbers = [2, 3, 3, 5, 6, 7, 9, 10]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
    print(uniques)