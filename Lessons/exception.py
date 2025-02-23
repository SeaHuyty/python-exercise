# Exception: use to handle errors or exceptions that are raised in our program.
age = int(input("Age: "))
print(age) # The code will be error if we enter 'str' instead of 'int'.
# That's the reason why we need to use exception.
try: 
    age = int(input("Age: "))
    income = 200
    risk = income / age # If user input age = 0, there will be another error names ZeroDivisionError.
    print(age)    
except ValueError: # except ValueError because that's the problem we have when user input different type of value.
    # Here we display a message when ValueError occurs.
    print("Invalid Value!!")
# If there are many types of error. We can add more excepts.
except ZeroDivisionError: 
    print("Age cannot be zero!")