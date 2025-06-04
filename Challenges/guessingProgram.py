# Exercise: Build a small guess program.
i = 1
print("Guessing a number game: the number is between 1-9")
while i <= 3:
    guess = input("Guess a number: ")
    if int(guess) == 9:
        print("Congratulation!! You won.")
        break
    i += 1
    if i > 3:
        print("Out of attempts!!")