# Question 52

# Define a class named Circle which can be constructed by a radius. 
# The Circle class has a method which can compute the area.

class Circle(object):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return ((2*22*self.radius*self.radius)//7)
    
area_circle = Circle(7)
print(area_circle.area())