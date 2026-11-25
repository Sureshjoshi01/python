# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.

def sum_of_num(n):
    if n:
        return n + sum_of_num(n - 1)
    else:
        return 0


sum = sum_of_num(10)
print(sum)