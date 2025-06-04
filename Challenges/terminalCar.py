# Exercise: Building a terminal car game.
index = 1
print("Welcome to car game!!")
print(">(start) to start your car\n>(stop) to stop your car\n>(quit) to close the game")
while index == 1:
    command = input(">")
    if command.lower() == 'start':
        print("Car start...Ready to go!!Vroom Vroom")
    elif command.lower() == 'stop':
        print("Car stopped!!")
    elif command.lower() == 'quit':
        quit()
    else:
        print("Invalid Command!!")