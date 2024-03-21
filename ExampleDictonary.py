phone = input("enter number: ")
digitsMapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}

output = ""

for character in phone:
    output += digitsMapping.get(character, "Doesnt exist!") + ""

print(output)