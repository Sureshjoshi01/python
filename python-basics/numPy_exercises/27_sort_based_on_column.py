# Exercise 27: Sorting a NumPy array based on a specific column


import numpy as np
sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

sorted_indices = sampleArray[:, 1].argsort()
print(sorted_indices)

sorted_array = sampleArray[sorted_indices]

print("Original array:")
print(sampleArray)

print("\nSorted array:")
print(sorted_array)