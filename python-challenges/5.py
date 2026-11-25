# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class test(object):
    def _init_(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())

    
strObj = test()
strObj.getString()
strObj.printString()

