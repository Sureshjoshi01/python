# Question 57

# Define a custom exception class which takes a string message as attribute.


class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")