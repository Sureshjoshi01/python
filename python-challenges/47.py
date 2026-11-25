# Question 47

# Write a program which can map() and 
# filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


def is_even(x):
    return x % 2 == 0

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(map(square, filter(is_even, numbers)))

print(result)
