# list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], find the common elements using sets.


list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]


set1 = set(list1)
set2 = set(list2)

common_ele = set1.intersection(set2)

print(common_ele)