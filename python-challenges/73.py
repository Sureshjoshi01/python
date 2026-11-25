# Question
# 73

# Please write a binary search function which searches an item in a sorted list. 
# The function should return the index of element to be searched in the list.


def binary_search(lst,item):
    lst = sorted(lst)
    mid = len(lst)//2
    if item == lst[mid]:
        return len(lst)//2
    elif item < lst[mid]:
        for i in range(0,mid):
            if item == lst[i]:
                return i
    elif item > lst[mid]:
        for i in range(mid,len(lst)):
            if item == lst[i]:
                return i


li=[2,5,7,9,11,17,222]
print(binary_search(li,7))
print(binary_search(li,11))

