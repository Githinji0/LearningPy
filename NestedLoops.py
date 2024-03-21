for x in range(10):
    for y in range(9):
        print(f'({x},{y})')

numbers = [2, 2, 2, 2, 5]

for x in numbers:
    output = ''
    for count in range(x):
        output = output + 'x'
    print(output)