# Exercise: Write a program to accept a string from the user and display characters that are present at an even index number.
#           For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
word = str(input("Enter a word: "))
length = int(len(word))
for item in range(0, length - 1, 2):
    i = item
    print(word[i])