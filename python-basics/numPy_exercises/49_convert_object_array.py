#Exercise 49: Convert to object array

#Convert a 1D array to an object array, retaining the original data type of each element.

import numpy as np
arr = np.array([1, 'a', 3, 4, 5]) 

obj_arr = np.empty(arr.size, dtype='object')

obj_arr[:] = arr

obj_arr[1] = 'a'
print(obj_arr)
print(obj_arr.dtype)