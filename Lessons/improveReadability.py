# Keyword Argument: We use Keyword Argument to improve the readability of our codes.
def greet_him(firstname, lastname):
    print(f"Hi {lastname} {firstname}")
    print("Welcome aboard")
greet_him("Wang", "Alex") # "Wang" and "Alex" are positional arguments.

def greet_her(firstname, lastname):
    print(f"Hi {lastname} {firstname}")
    print("Welcome aboard")
greet_her(lastname="Dha", firstname="Retica") # This is keyword argements.