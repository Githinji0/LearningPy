#we use the try exception
try:
    age = int(input("Enter your age:"))
    income = 20000
    risk = income / age
    print(risk)
# this is an error caused by age being zero
except ZeroDivisionError:
    print("Invalid Age")
#whwen the user puts in an non interger value as the age
except ValueError:
    print("invalid value")
