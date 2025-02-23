# Return Statement: Use to return something from the function.
number = int(input("Input a number: "))
def square(number):
    return number * number
print(f"Square of {number} is: {square(number)}")
# If we don't have return in a function. Python will return 'None'