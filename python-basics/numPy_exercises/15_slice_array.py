# Write a code to Create a 4×4 NumPy array and extract the first two rows and first two columns.

import numpy as np

arr = np.arange(1,17).reshape(4,4)

print(arr)

print(arr[0:2,0:2])