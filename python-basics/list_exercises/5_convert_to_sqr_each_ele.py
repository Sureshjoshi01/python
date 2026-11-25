# Given a list of numbers. write a program to turn every item of a list into its square.

numbers = [1, 2, 3, 4, 5, 6, 7]

squared_list = []
for i in numbers:
    i = i * i
    squared_list.append(i)

print(squared_list)