# Write a recursive function to calculate the factorial of a non-negative integer.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

    
print(factorial(5))


