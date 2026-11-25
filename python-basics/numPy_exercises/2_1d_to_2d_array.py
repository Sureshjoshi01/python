# Write a code to convert a 1D array to a 2D array with 2 rows.

import numpy as np
arr = np.arange(6)

print("Original Array: ",arr)
reshaped_array = arr.reshape(2,3)
print("Reshaped 2x3 Array :",reshaped_array)