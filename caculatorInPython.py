import math
#operation functions
def additionOperation():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    #sum = num1 + num2
    #Difference = num1 - num2
    #Product = num1 * num2
    #Quotient = num1 // num2
    #Remainder = num1 % num2

    #print("the sum is: ", sum)
    #print("the Difference is: ", Difference)
    #print("the Product is: ", Product)
    #print("the Quotient is: ", Quotient)
    #print("the Remainder is: ", Remainder)

def binary_operations():
    num1 = int(input("Enter the first binary number: "), 2)
    num2 = int(input("Enter the second binary number: "), 2)

    print("Sum:", bin(num1 + num2)[2:])
    print("Difference:", bin(num1 - num2)[2:])
    print("Product:", bin(num1 * num2)[2:])
    print("Quotient:", bin(num1 // num2)[2:])
    print("Remainder:", bin(num1 % num2)[2:])

def hexadecimal_operations():
    num1 = int(input("Enter the first hexadecimal number: "), 16)
    num2 = int(input("Enter the second hexadecimal number: "), 16)

    print("Sum:", hex(num1 + num2)[2:])
    print("Difference:", hex(num1 - num2)[2:])
    print("Product:", hex(num1 * num2)[2:])
    print("Quotient:", hex(num1 // num2)[2:])
    print("Remainder:", hex(num1 % num2)[2:])

def octal_operations():
    num1 = int(input("Enter the first octal number: "), 8)
    num2 = int(input("Enter the second octal number: "), 8)

    print("Sum:", oct(num1 + num2)[2:])
    print("Difference:", oct(num1 - num2)[2:])
    print("Product:", oct(num1 * num2)[2:])
    print("Quotient:", oct(num1 // num2)[2:])
    print("Remainder:", oct(num1 % num2)[2:])

def main():
    print("1. Binary Operations")
    print("2. Hexadecimal Operations")
    print("3. Octal Operations")
    print("4. Normal Sum")

    choice = int(input("Enter your choice (1-4): "))
    #print()

    if choice == 1:
        binary_operations()

    elif choice == 2:
        hexadecimal_operations()
        
    elif choice == 3:
        octal_operations()

    elif choice == 4:
        additionOperation()

    else:
        print("Invalid choice. Please enter a number from 1 to 4 !")

if __name__ == '__main__':
    main()