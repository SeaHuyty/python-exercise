# Calculate and output the BMI (Body Mass Index) by obtaining the user's name, height, weight.
# BMI is calculated by dividing one's weight by the square of their height and the formula is kg/m^2.
name = str(input("Enter your name: "))
height = int(input("Enter your height (cm): "))
weight = int(input("Enter your weight (kg): "))
bmi = weight / (height ** 2) * 10000
print(f"Your Body Mass Index: {bmi}")