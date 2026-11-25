# Write a code to remove items from set1 that are not present in set2.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)

print(set1)