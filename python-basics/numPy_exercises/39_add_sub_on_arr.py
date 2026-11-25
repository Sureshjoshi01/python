# Exercise 39: Perform Addition and Squaring on Arrays

import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

arr_add = np.add(arrayOne,arrayTwo)

print(arr_add)

arr_sq = np.square(arrayOne,arrayTwo)
print(arr_sq)