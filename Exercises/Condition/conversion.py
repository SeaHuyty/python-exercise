# Exercise: Convert weight from Kilogram to Pound or from Pound to Kilogram.
weight = input("Please enter your weight: ")
measurement_of_weight = input("(K)g or (l)bs: ")
if (measurement_of_weight.lower() == 'k'):
    weight = float(weight) * 2.20
    print("Your weight in lbs:", float(weight), "lbs")
elif (measurement_of_weight.lower() == 'l'):
    weight = float(weight) // 2.20
    print("Your weight in kg:", float(weight), "kg")
else:
    print("Invalid measurement!!")