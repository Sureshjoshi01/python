# Question 72

# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.

# Hints: Use if/elif to deal with conditions.

def binary_search(l,item):
    for i in range(len(l)+1):
        if item == int(l[i]):
            return i
        else:
            print("Item Not in List") 

n = input()
l = n.split(" ")
print(l)
print("Enter item to be searched in list : ",end="")
item = int(input())
binary_search(sorted(l),item)