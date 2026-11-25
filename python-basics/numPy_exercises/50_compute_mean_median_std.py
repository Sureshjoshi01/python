# Exercise 50: Compute the mean, median, and standard deviation of a NumPy array

import numpy as np
arr = np.array([10, 20, 30, 100, 200, 300])

men = np.mean(arr)
med = np.median(arr)
st_d = np.std(arr)

print(men,med,st_d)