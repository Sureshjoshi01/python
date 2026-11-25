#Exercise 21: Compute the mean, median, and standard deviation of a NumPy array
   # Mean: Average of numbers.
   # Median: Middle value when sorted.
   # Standard Deviation: How spread out values are from the mean.


import numpy as np
arr = np.array([10, 20, 30, 100, 200, 300])

mean = 0 
n = len(arr) 
for i in arr:
    mean = mean + i

median = np.median(arr)
std = np.std(arr)
print("Mean :",mean/n)
print("Median :",median)
print("Standard Deviation :", std)



