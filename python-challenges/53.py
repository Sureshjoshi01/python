# Question 53

# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class rectangle:
    def area(self,length,width):
        self.length = length
        self.width = width
        area = length * width
        return area 


print("Enter length of the rectange : ", end="")
l = int(input())
print("Enter width of the rectange :",end="")
w = int(input())
rect = rectangle()  
print("Area of rectange : ",rect.area(l,w))
    