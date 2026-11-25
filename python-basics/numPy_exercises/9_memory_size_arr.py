# Exercise 9: Find the memory size of a NumPy array of numbers from 0 to 9

import numpy as np 

arr = np.arange(0,10)

print("Array: ", arr)
print("Memory size in bytes: ",arr.nbytes)