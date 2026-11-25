#Use list comprehension to create a new list containing only the numbers from a given list

# without using list comprehension

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new_list = []
for i in my_list:
    if isinstance(i, (int, float)):
        new_list.append(i) 

print(new_list)

# with list comprehension

numbers_only_list = [item for item in my_list if isinstance(item, (int, float))]
print(f"List containing only numbers: {numbers_only_list}")