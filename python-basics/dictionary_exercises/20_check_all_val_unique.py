# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.

def unique_dict(dict1):
    lst = []
    for i in dict1:
        lst.append(dict1[i])
    l = len(lst)
    for i in range(l):
        for j in range(i+1,l):
            if lst[i] == lst[j]:
                return False
    return True


dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
print("Dictionary:", dict1, "-> All values unique?", unique_dict(dict1))
dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
print("Dictionary:", dict2, "-> All values unique?", unique_dict(dict2))
dict3 = {} # Empty dictionary (all values are vacuously unique)
print("Dictionary:", dict3, "-> All values unique?", unique_dict(dict3))