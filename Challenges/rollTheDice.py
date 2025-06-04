# Exercise: Create a roll the dice program.
print("Let's gamble")
print("We're gonna roll 2 dices, And you guess the number with what you want to do.")
print("Example: You want to commit suicide and you guess (3, 6), so if the dices are (3, 6) or (6, 3) then you should commit suicide!!")
decision = str(input("Do you want to play? (Yes/No)\n=>"))
if decision.lower() == 'yes':  
    import random
    guess_01 = input("Guess the first dice: ")
    guess_02 = input("Guess the second dice: ")
    print(f"So you guessed: ({guess_01}, {guess_02})")
    k = 0
    while k != 1:
        roll = str(input("Now type (roll) to roll the dice: "))
        if roll.lower() == "roll":
            dice_01 = random.randint(1, 6)
            dice_02 = random.randint(1, 6)
            print(f"({dice_01}, {dice_02})")
            if (guess_01 == dice_01 or guess_01 == dice_02) and (guess_02 == dice_01 or guess_02 == dice_02):
                print("There you go!!")
            k = 1
        else:
            print("Type again!")
else:
    quit()