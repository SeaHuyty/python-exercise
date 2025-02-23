# Constructors: A constructor is a function that called at the time of creating an object.
class Point:
    def __init__(self, x, y): # That init stand between two underscores.
        self.x = x
        self.y = y
point = Point(10, 20)
print(point.x)
print(point.y)
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm your top G {self.name}") # We have to add the parameter.
alex = Person("Alexis Wang")
print(alex.name)
alex.talk()

lorses = Person("Lorses Lead")
print(lorses.name)
lorses.talk()