import math

def addition(num1,num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

print("1.Addition:")
print("2.subtraction:")
print("3.Multiplication:")
print("4.Division:")
print("5.Quit")

operation = int(input("Choose the operation: "))
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

if operation == 1:
        print(f'the answer is: {addition(num1, num2)}')

elif operation == 2:
        print(f'the answer is: {subtraction(num1, num2)}')

elif operation == 3:
        print(f'the answer is: {multiply(num1, num2)}')

elif operation == 4:
        print(f'the answer is: {divide(num1, num2)}')
else:
        print("Select an number in the above")

