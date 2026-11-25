# Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
print(f"Original tuple: {tuple1}")

# Convert the tuple to a list because tuples are immutable and cannot be sorted in-place
list1 = list(tuple1)

# Sort the list using the 'sorted()' function with a lambda key
# The lambda function `lambda item: item[1]` tells sorted() to use the second element
# (index 1) of each inner tuple for comparison.
sorted_list = sorted(list1, key=lambda item: item[1])

# If you need the result back as a tuple, convert the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)

print(f"Sorted tuple by 2nd item: {sorted_tuple}")