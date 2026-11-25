# Exercise 26: Create a random 3×2 matrix and find its maximum and minimum values

import numpy as np
import random

for i in range(3):
    print()
    for j in range(2):
        print(i,end="")


print()
arr = np.random.rand(3,2)
print(arr)
print("min :",np.min(arr))
print("max :",np.max(arr))

