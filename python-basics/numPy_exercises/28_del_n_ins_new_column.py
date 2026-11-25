# Exercise 28: Delete and Insert a Column in a NumPy Array

import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumnToAdd = np.array([10, 10, 10])

del_arr = np.delete(sampleArray,1,axis=1)
resultArray = np.insert(del_arr, 1, newColumnToAdd, axis=1)

print(resultArray)