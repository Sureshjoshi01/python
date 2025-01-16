# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

import random

num = []
n = int(input("Enter list size : "))
for i in range(n):
    num.append(random.randint(1,100))

print("Original list : ", num)

even_lst = []
for i in num:
    if i % 2 == 0:
        even_lst.append(i)

print("List containing only even number : ",even_lst )
