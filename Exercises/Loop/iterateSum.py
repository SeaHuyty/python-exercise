# Exercise: Write a program to iterate the first 10 numbers, and in each iteration,
#           print the sum of the current and previous number.
i = 0
print(f"\nStart from {i}\n")
while i <= 10:
    i += 1
    print(f"Current number: {i}, Previous Number: {i-1}, Sum: {i+i-1}\n")