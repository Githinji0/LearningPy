command = ""
started = False

while True:
    command = input(">> ").lower()

    if command == "start":
        if started:
            print("The car is allready started!!")

        else:
            started = True
            
        print("The car has started..")

    elif command == "stop":
        if not started:
            print("car is already stoped")

        else:
            started = False
        print("The car has stoped!")

    elif command == "Help":
        print(
            """ Type start to start car
                Stop to strop the car
                Quit to quit program
            """
            )
        
    elif command == "quit":
        break

    else:
        print("sorry command doesnt match")
        
        
