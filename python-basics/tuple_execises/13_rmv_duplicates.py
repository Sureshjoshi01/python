# Write a code to create a new tuple with only unique elements

my_tuple = (1, 2, 2, 3, 4, 4, 5)

print("Original tuple with duplicates:", my_tuple)
print("Tuple with unique elements:", tuple(set(my_tuple)))
