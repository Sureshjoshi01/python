#Write a Python program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

def sum_of_nums(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum


n = int(input("Enter number : "))

print("sum of all numbers from 1 to number entered : ", sum_of_nums(n) )
