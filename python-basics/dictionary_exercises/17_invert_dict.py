# Write a code to swap keys and values in a dictionary. Assume all values are unique

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

keys = []
for k in original_dict1:
    keys.append(k)

values = []
for v in original_dict1:
    values.append(original_dict1[v])
    
print(keys)
print(values)

new_dict = {}
for i in range(len(values)):
    new_dict.update({values[i]: keys[i] })

print(new_dict)
