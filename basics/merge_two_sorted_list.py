# Write a function to merge two sorted lists into a single sorted list.

import random

# Generate first list of random numbers
def first_list():
    list1 = []
    for i in range(0,3):
        list1.append(random.randint(1,100))
    return list1

# Generate first list of random numbers
def second_list():
    list2 = []
    for i in range(0,10):
        list2.append(random.randint(1,100))
    return list2

# Sort and merge lists
def sort_n_merge(list1,list2):
    len1 = len(list1)
    len2 = len(list2)
    print("original list 1 --->", list1)
    print("original list 2 --->", list2)
    list1.sort()
    list2.sort()
    print("sorted list 1 --->", list1)
    print("sorted list 2 --->", list2)
    for i in list2:
        list1.append(i)
    print("merged list :", list1)
    list1.sort()
    set(list1)
    print("sorted merged list :", list(list1))

def main():
    list1 = first_list()
    list2 = second_list()
    sort_n_merge(list1,list2)
    
main()




