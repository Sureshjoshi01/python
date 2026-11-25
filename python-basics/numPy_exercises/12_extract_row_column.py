# Exercise 12: Create a 4×4 array and extract its first row and last column

import numpy as np

arr = np.arange(1,17).reshape(4,4)

print("Array:",arr)

print("First row :", arr[0])
print("last row:", arr[:,-1])