# Write a code to extract all numbers from an array that are between 5 and 10 (inclusive).

import numpy as np
arr = np.arange(15)

for i in arr:
    if i>=5 and i<=10:
        print(i,end=" ")
print("\n")
print(arr[5:11])