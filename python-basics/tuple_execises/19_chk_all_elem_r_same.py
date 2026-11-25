# Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

count = tuple1.count(45)
l = len(tuple1)

if l == count:
    print(True)
else:
    print(False)