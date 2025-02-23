# Inheritance: Inheritance is a mechanism for using code. With Inheritance, we don't need to rewrite function many times.
class Mammal:
    def walk(self):
        print("Walk")
    
class Dog(Mammal): # Here the dog class will inherit all the methods defined in the Mammal class.
    # Python don't like having nothing in the block of classes.
    # So we can use (pass) to make Python happy.
    pass
class Cat(Mammal): # The cat here will also inherit from the Mammal Class.
    # We can also add a specific method refer to cat.
    def hiss(self):
        print("Hiss")
    def be_annoying(self):
        print("Annoying")
    def lazy(self):
        print("Lazy")
    # If we already have something in our class, we don't need to use (pass)
dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.hiss()
cat1.walk()