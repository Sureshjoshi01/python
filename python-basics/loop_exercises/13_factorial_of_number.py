# Write a Python program to use for loop to find the factorial of a given number.

def factorial(n):
    fact = 1
    if n < 0:
        print("Factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact = fact * n
            n = n - 1
        return fact

n = int(input("Enter number whose factorial is required : "))
print(factorial(n))

