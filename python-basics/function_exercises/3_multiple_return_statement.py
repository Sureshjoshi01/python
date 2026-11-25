# Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.

def calculation(a,b):
    sum = a + b
    if a > b:
        sub = a - b
    else:
        sub = b - a
    return sum,sub

addition,subtraction = calculation(50,30)
print(addition)
print(subtraction)

