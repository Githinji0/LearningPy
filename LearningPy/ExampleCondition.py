Name = input("enter your name: ") #user inputs

if len(Name) < 2:
    print("name cant be shorter than 3 letters")
elif len(Name) > 30:
    print("NAME CANT BE LONGER THAN 30 LETTERS")
else:
    print("wellcome! ")