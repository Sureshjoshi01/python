# Exercise 17: Get the indices of non-zero elements in an array

import numpy as np
arr = np.array([1, 0, 2, 0, 3, 0, 4])

print("Array:",arr)

non_zero = np.nonzero(arr)
print(non_zero)