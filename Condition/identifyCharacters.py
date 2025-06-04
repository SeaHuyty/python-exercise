# Exercise: Get input as character then check whether a given character is a vowel or consonant.
print("We are going to determine if the character you input is a vowel or a consonant.")
character = str(input("Please input the character: "))
character = character.lower()
if (character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
    print(f"{character} is a vowel!!")
else:
    print(f"{character} is a consonant!!")