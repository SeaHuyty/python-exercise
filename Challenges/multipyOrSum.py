# Exercise: Calculate the multiplication and sum of two numbers:
#           Given two integer numbers, return their product only if the product is equal to or lower than 1000. 
#           Otherwise, return their sum.
def multiply(number_01, number_02):
    return number_01 * number_02

def total(number_01, number_02):
    return number_01 + number_02


number_01 = int(input("Enter the first number: "))
number_02 = int(input("Enter the second number: "))
if number_01 * number_02 <= 1000:
    print(multiply(number_01, number_02))
else:
    print(total(number_01, number_02))