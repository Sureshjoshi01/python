#Exercise 1: Calculate the multiplication and sum of two numbers
#Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
sum = a + b
mult = a * b
if mult <= 1000:
    print("the result is",mult)
else:
    print("the result is",sum)
