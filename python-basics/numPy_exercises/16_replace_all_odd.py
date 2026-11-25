# Exercise 16: Replace all odd numbers in a NumPy array with -1

import numpy as np 

arr = np.arange(1,11)

print("Original Array:",arr)

for i in range(len(arr)):
    if (i%2) == 1:
        arr[i] = -1

print("Modified Array:",arr)
