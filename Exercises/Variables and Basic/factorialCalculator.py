# Exercise: Read input from user (n) then calculate Factorial of input n then write the results.
print("This code will calculate factorial of the integer you input.")
user_in = int(input("Please enter an integer number: "))
import math
print(f"Factorial of {user_in} = {math.factorial(user_in)}")