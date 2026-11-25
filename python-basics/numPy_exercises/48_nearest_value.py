#Exercise 48: Find nearest value

#Find the value in an array that is closest to a number 3.


import numpy as np
arr = np.array([1.5, 2.8, 3.2, 4.1])

import numpy as np

arr = np.array([1.5, 2.8, 3.2, 4.1])
target_value = 3

# Find the index of the minimum absolute difference
index = np.abs(arr - target_value).argmin()

# Use the index to get the value
nearest_value = arr[index]
print(f"The value closest to {target_value} is: {nearest_value}")