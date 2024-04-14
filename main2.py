even_numbers = []
for number in range(20):
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)

odd_numbers = [number for number in range(20) if number % 3 == 0]

print(odd_numbers)