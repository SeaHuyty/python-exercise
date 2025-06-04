# Exercise: Get name input from user and determine if the name meet the requirement.
print("Username should be between 6 to 14 letter and number!!")
user_input = input("Please enter your username: ")
if len(user_input) < 6:
    print("Your username is too short!!")
elif len(user_input) > 14:
    print("Your username is too long!!")
else:
    print(f"Hello Ms/Mr {user_input}")