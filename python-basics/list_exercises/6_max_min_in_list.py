# Find and print the largest and smallest number in a list

data = [8, 2, 15, 1, 9]

max = data[0]
min = data[0]

for i in data:
    if i > max:
        max = i
    elif i < min:
        min = i

print("Largest number:", max)
print("Smallest number:", min)  