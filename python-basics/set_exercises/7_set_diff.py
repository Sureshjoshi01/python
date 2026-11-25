# Given two Python sets, write a program to update the first set with only the items that are unique to it (i.e., not present in the second set).

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)

print(set1)