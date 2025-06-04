# Exercise: Use selection statement to check the age of user and determine if they are eligible to vote.
age = input("Please enter your age: ")
if (0 < int(age) < 18):
    print("You're not eligible to vote!!")
elif (int(age) < 0):
    print("Invalid!!")
else:
    print("You're eligible to vote!!")