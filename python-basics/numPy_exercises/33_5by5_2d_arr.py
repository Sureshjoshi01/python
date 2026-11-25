# Exercise 33: Create a 5×5 2D array with 1s on the border and 0s inside.

import numpy as np

arr = np.ones(25).reshape(5,5)
print(arr)

arr[1:-1, 1:-1] = 0
print()
print(arr)