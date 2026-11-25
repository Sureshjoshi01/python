#Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number

sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
print("Original List : ", sample_list)

print("unique items", (list(set(sample_list))))
print("tuple", (tuple(set(sample_list))))

max = sample_list[0]
min = sample_list[0]

for i in sample_list:
    if i > max:
        max = i
    elif i < min:
        min = i

print("min:", min)
print("max:", max)
