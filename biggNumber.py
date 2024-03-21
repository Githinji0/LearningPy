numbers = [1, 2, 3, 4, 5]
bigNumber = numbers[0]

for number in numbers:
    if number > bigNumber:
        bigNumber = number
print(bigNumber)