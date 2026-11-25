# Exercise 22: Remove common items from array

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])

# Create a boolean mask where `a`'s elements are NOT in `b`
mask = np.isin(a, b)

# Use the `~` operator to invert the mask (get the opposite)
result = a[~mask]
print(result)