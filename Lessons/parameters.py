# Parameter: A parameter is what we have at the time of declaration.
def greet_user(name): # (name) here is a parameter.
    print(f"Hi {name}")
    print("Welcome aboard")
print("Start")
greet_user("John") # We are obligated to pass value for parameter.
greet_user("Mary") # Mary and John here are arguments.
print("Finish")
def greet_him(firstname, lastname):
    print(f"Hi {lastname} {firstname}")
    print("Welcome aboard")
greet_him("Wang", "Alex")