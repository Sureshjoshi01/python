# Exercise 10: Reverse a 1D NumPy array

import numpy as np 

lst = []
arr = np.arange(10)
print("Original Array: ",arr)

for i in range(len(arr)-1,-1,-1):
    lst.append(arr[i])

print(lst)
rev_arr = np.array(lst)
print("Reversed Array:",rev_arr)