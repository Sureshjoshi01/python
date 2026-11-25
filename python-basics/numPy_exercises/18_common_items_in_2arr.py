# Exercise 18: Find the common items between two arrays

import numpy as np
lst = set()
a = np.array([1, 2, 3, 2, 8, 4, 2, 4])
b = np.array([2, 4, 5, 6, 8])

new_arr = np.intersect1d(a,b)

print(new_arr)