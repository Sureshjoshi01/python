# While we know how to check for a key’s presence in a dictionary, it’s sometimes necessary to determine if a specific value exists.

# Write a Python program to check if the value 200 is present in the provided dictionary.


sample_dict = {'a': 100, 'b': 200, 'c': 300}

for k in sample_dict:
    if sample_dict[k] == 200:
        print("200 present in a dict")