# Exercise 31: Create a 3×3 array of random integers and sort it row-wise

import numpy as np

arr = np.random.randint(1,100,size=(3,3))
sorted_arr = np.sort(arr,axis=1)

print(sorted_arr)