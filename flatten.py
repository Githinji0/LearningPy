matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_list = []

for row in matrix:
    for number in row:
        flattened_list.append(number)
print(flattened_list)
# alt list comprehensive

flatten = [number for row in matrix for number in row]
print(flatten)
