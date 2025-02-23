# Exercise: (Bonus) You're learning about Cambodian greetings (Choum reap sor) and want to practice using Sampeah.
# Write a program that:
# • Prompts the user to enter the age of the person they are greeting.
# • Presents a menu with numbered options for the social status of the person:
# a. Friend
# b. Elder/Senior/Boss
# c. Parent/Grandparent/Teacher
# d. King/Monk
# e. God/Sacred Statue
# • Asks the user to enter the corresponding number representing the social status.
# • Uses a switch statement to check the entered social status code:
#  − Case 1: Friend (Sampeah level 1)
#  − Case 2: Elder/Senior/Boss (Sampeah level 2)
#  − Case 3: Parent/Grandparent/Teacher (Sampeah level 3)
#  − Case 4: King/Monk (Sampeah level 4)
#  − Case 5: God/Sacred Statue (Sampeah level 5)
#  − Default: Handle invalid input and suggest referring to the menu options.
# • Prints a message describing the recommended Sampeah level based on the age and social status information.
# This exercise focuses on using a switch statement to determine the appropriate Sampeah level based on user input
# (age and social status represented by numbers).
print("This program will help you learn about Cambodian greeting.")
age = input("Please enter the age of they person you're greeting: ")
print("Social status of the person:\na. Friend\nb. Elder/Senior/Boss\nc. Parent/Grandparent/Teacher\nd. King/Monk\ne. God/Sacred Statue")
select = str(input("=> Select the social status of the person: "))
def selected_case(select):
    if select.lower() == 'a':
        return "Recommend Chest Level: It is used when you greet friends or other people of the same age or status by placing the budding lotus's hands on the chest."
    elif select.lower() == 'b':
        return "Recommend Mouth Level: The second one is mostly seen in the palms' positioning on the mouth. It is utilized to greet, thank you, sorry, or say goodbye to people with higher statuses, such as older relatives, bosses, and so on."
    elif select.lower() == 'c':
        return "Recommend Nose Level: The third Sampeah is put at the nose with a head bowing down a little bit. This gesture must be used to show respect to parents, grandparents, teachers, or the elderly."
    elif select.lower() == 'd':
        return "Recommend Eyebrow Level: The fourth one is for respecting the king, monks, or female and male monastics."
    elif select.lower() == 'e':
        return "Recommend Forehead Level: In the case of praying to Buddha, Gods, sacred statues, or temples."
print(selected_case(select))