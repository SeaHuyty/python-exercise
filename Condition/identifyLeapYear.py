# Exercise: Get input as year then check if the input year is the leap year or not.
print("We are going to determine if the year you input is a leap year or not")
year = int(input("Please enter a year: "))
if (year % 4 == 0 and year % 400 != 0 and year % 100 == 0):
    print("It's not a leap year")
elif (year % 4 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")