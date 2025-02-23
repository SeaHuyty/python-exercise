# Exercise: Write a program that asks for a phone number and then convert the number to word.
print("We will convert the number you enter to word.")
phone = input("Enter your number: ")
digit_number = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
} # You can continue to all the decimal number. I'm just lazy.
output = ""
for character in phone:
    # We use .get(character, '!') in case there ain't the key, so we will supply it with '!'.
    output += digit_number.get(character, '!') + " "
print(output.title())