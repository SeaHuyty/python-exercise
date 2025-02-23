# Exercise: Write a program to remove the duplicates in a list.
numbers = [6, 5, 4, 3, 6, 5, 4 ,3]
uniques = [] # We use a new list to filter the duplicate number.
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)