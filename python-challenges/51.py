# Question 51

# Define a class named American and its subclass NewYorker.

class American(object):
    @staticmethod
    def printNationality():
        print("America")

class NewYorker(American):
    pass

anAmerican = American()
anAmerican.printNationality()
American.printNationality()
