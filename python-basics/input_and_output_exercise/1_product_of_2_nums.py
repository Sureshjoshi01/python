#Write a program to accept two integer numbers from the user and calculate their product.

def product_of_two_nums(x,y):
    product = x*y
    return product

x = int(input("Enter Firt number : "))
y = int(input("Enter second number : "))
print("Product of",x,"and",y,":", product_of_two_nums(x,y))