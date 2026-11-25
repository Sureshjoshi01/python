#Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.

sample_list = [34, 54, 67, 89, 11, 43, 94]

x = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)

sample_list.insert(2,x)
print("List After removing element at index 4 ", sample_list)

sample_list.append(x)
print("List After removing element at index 4 ", sample_list)



