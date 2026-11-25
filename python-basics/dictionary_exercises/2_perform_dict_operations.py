#Perform following operations on given dictionary
#Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
#Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary




my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

del my_dict['profession']
print("Original dictionary:", my_dict)

print("Updated dictionary after removing 'profession':", my_dict)

print("Printing all key-value pairs:")
for k in my_dict:
    print(k,":",my_dict[k])

print("Does 'age' exist?",end =' ')
for k in my_dict:
    if k == 'age':
        print("True")
        break