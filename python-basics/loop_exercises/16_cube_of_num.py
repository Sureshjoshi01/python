# Write a Python program to print the cube of all numbers from 1 to a given number

def cube(n):
    for i in range(1,n+1):
        cub = i * i * i
        print("Current Number is :", i,  "and the cube is :", cub)


n = int(input("Enter Number : "))
cube(n)
