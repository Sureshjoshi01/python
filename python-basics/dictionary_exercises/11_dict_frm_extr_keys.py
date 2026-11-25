# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

new_dict = {}
for k in keys:
    new_dict.update({k: sample_dict[k]})


print(new_dict)