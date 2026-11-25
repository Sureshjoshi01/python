# Perform following operations on given dictionary
# Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
# Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
# Access Key: Print the value associated with the city key.


my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}


print("Original dictionary:", my_dict)

my_dict['profession'] = 'Doctor'
print("Updated dictionary after adding 'profession':", my_dict)

my_dict['age'] = 40
print("Updated dictionary after modification:", my_dict)

print("City:", my_dict['city'])

