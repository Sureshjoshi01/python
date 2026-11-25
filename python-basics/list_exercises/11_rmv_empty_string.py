# Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1:
    if len(i) == 0:
        list1.remove(i)

print(list1)