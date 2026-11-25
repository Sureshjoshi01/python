# Question 95

# Define a class Person and its two child classes: Male and Female. 
# All classes have a method "getGender" which can print "Male" for Male class 
# and "Female" for Female class.

class person():
    def getGender(self):
        return None
class Male(person):
    def getGender(self):
        return "Male"
class Female(person):
    def getGender(self):
        return "Female"


m = Male()
print(m.getGender())
f = Female()
print(f.getGender())

