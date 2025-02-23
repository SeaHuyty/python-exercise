# Exercise:  Write a C program using any type of loop that repeatedly prompts the user for positive integers (greater than 0)
#            until a non-positive number is entered, and then prints the total count of positive numbers entered.
print("This program allows you to enter positive numbers and it'll count the numbers you entered.")
print("Note: If you want to stop, please enter a negative number")
i = 1
count = 0
while i >= 0:
    number = int(input("Input a number: "))
    if number >= 0:
        count += 1
    else:
        i = -1
print(f"Total positive number you entered: {count}")