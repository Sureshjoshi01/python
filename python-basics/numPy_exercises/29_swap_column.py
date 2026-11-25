#Exercise 29: Swap column 1 and 2 in a 2D array

import numpy as np
arr = np.arange(9).reshape(3, 3)
print(arr)
arr[:, [1, 2]] = arr[:, [2, 1]]
print("After")

print(arr)