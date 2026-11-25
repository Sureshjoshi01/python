# Exercise 35: Sort the rows of a 2D array based on the values of the second column

import numpy as np
arr = np.array([[8, 4, 1],
                [5, 2, 7],
                [6, 9, 3]])

sorted_indices = arr[:, 1].argsort()

# Use the indices to sort the entire array's rows
sorted_arr = arr[sorted_indices]
print(sorted_arr)