secretNumber = 7
trials = 0
limit = 3

while trials < limit:
    answer = int(input("Guess the number: "))
    trials = trials + 1
    if answer == secretNumber:
        print("Correct!!")
        break #terminates the loop
else:
    print("Sorry you failed!!")
        

