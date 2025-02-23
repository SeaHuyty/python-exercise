# Exercise: Get input from user 3 integers number a, b, and c then find the max number and print the max number.
print("We're going to find a max number from the number you input. Note: Input integer!!")
a = input("Please input the first integer: ")
b = input("Please input the second integer: ")
c = input("Please input the third integer: ")
if (a > b and a > c):
    print(f"{a} is the max or the biggest number!!")
elif (b > a and b > c):
    print(f"{b} is the max or the biggest number!!")
else:
    print(f"{c} is the max or the biggest number!!")