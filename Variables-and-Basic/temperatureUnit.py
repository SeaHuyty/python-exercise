# Temperature Conversion: Fahrenheit to Celsius: Prompt the user to input a temperature value as Fahrenheit, perform the conversion from Fahrenheit to Celsius
#                                                using appropriate formulas, and display the converted temperature. Tips: °C = ( °F - 32) ÷ 9/5
print("We'll convert temperature in Fahrenheit to Celsius")
fahrenheit = input("Please input temperature in Fahrenheit: ")
celsius = ((float(fahrenheit) - 32) * 5/9)
print(f"So temperature in Celsius: {celsius}")