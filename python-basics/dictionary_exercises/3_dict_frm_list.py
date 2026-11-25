# Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = {}
n = 0
for i in keys:
    my_dict[i] = values[n]
    n = n + 1

print(my_dict)

