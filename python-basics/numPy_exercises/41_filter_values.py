#Exercise 41: Use boolean indexing to filter values less than a given number

import numpy as np
lt = []
arr = np.array([5, 12, 29, 30, 44, 7, 18])

#1. 
for i in range(len(arr)):
    if arr[i] < 30:
        lt.append(int(arr[i]))

print("Values < 30:", lt)

#2. 
filtered = arr[arr<30]
print("Values < 30:", filtered)