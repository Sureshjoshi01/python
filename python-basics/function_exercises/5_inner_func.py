# Create a program with nested functions to perform an addition calculation as follows:

#    Define an outer function that accepts two parameters, a and b.
#    Inside this outer function, define an inner function that calculates the sum of a and b.
#    The outer function should then add 5 to this sum.
#    Finally, the outer function should return the resulting value.

def outer_func(a,b):
    def inner_func():
        sum = a + b
        return sum
    sum = inner_func() + 5
    return sum

sum1 = outer_func(10,15)
print(sum1)
