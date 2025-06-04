# Exercise: Write a program to find the largest and the smallest number in a list.
numbers = [10, 20, 40, 30, 80, 50]
largest = numbers[0]
smallest = numbers[4]
# We give them value because we need to use a number to compare with a the number in the list.
for k in numbers:
    if k > largest:
        largest = k
    if k < smallest:
        smallest = k
print(f"Largest number in the list is {largest} and smallest number is {smallest}")