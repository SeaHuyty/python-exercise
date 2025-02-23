# Classes: We use Classes to define new type.
class Point: # In class we capitalize every first letter of the word or we can say write in Pascal case.
    def move(self): # The function (move) uses to move a point.
        print("Move")
    
    def draw(self):
        print("Draw") 
point1 = Point() # point1 is an object.
point1.draw()
# Or
point1.x = 10 # This here means we set the x attribute of this point object.
point1.y = 20
print(f"{point1.x} and {point1.y}")
# We can create point2
point2 = Point()
point2.move()
point2.z = 30
print(point2.z)