# Exercise: Create a Russian Roulette Game.
print("Let's gamble")
print("We're gonna put let you put 2 bullets randomly in a the gun.")
print("Then we'll place the gun toward your head and pull the trigger.")
decision = str(input("Do you want to play? (Yes/No)\n=>"))
if decision.lower() == 'yes':  
    import random
    bullet_01 = int(input("Place the bullet in one of the 6 column: "))
    bullet_02 = int(input("Place another one in the 5 remained column: "))
    k = 0
    while k != 1:
        roll = str(input("Now type (roll) to roll the the bullet: "))
        if roll.lower() == "roll":
            trigger = random.randint(1, 6)
            print(f"{trigger}")
            if (trigger == bullet_01):
                print("You Die!!")
                k = 1
            elif (trigger == bullet_02):
                print("You Die!!")
                k = 1
            else:
                print("Missed!!")
        else:
            print("Type again.")
else:
    quit()