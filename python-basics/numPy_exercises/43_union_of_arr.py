#Exercise 43: Find the intersection and union of two arrays

#    Intersection: elements present in both arrays.
#    Union: all unique elements from both arrays, sorted.

import numpy as np

a = np.array([1, 2, 3, 5, 7])
b = np.array([3, 4, 5, 6, 7])


c = np.intersect1d(a,b)
print(c)

d = np.union1d(a,b)
print(d)