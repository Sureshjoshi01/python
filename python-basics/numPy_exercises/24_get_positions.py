# Exercise 24: Get the positions where elements of array a and b match

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 4, 3, 7, 8])

lst = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j] and i==j:
            lst.append(i)

print(lst)


index = np.where(a == b)
print(index)