# Write a code to filter out students with scores less than 90 from a given a list of tuples.

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

lst = []
for i in students:
    if i[1] < 90:
        lst.append(i)

print(lst)