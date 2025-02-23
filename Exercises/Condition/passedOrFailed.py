# Exercise:  Write a C program that prompts the user to input the scores of five subjects, calculates the total marks obtained,
#            determines whether the student passed or failed (passing marks >= 50) using if-else statement.
print("We will determine whether you pass or fail base on the score of your five subjects.")
print("Please input the score of your subjects: (Note: Maximum score of each subject is 20)")
math = input("\tMathematic: ")
physic = input("\tPhysic: ")
chemistry = input("\tChemistry: ")
history = input("\tHistory: ")
english = input("\tEnglish: ")
sum = int(math) + int(physic) + int(chemistry) + int(history) + int(english)
if sum >= 50:
    print(f"Your total score is {sum}/100, You passed!!")
else:
    print(f"You got {sum}/100, You failed!!")