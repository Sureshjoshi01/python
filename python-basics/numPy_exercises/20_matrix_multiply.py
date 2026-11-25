#Exercise 20: Matrix multiplication

# Write a code to compute the dot product of two NumPy arrays


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product = 0

for i in range(len(a)):
        dot_product = dot_product + (a[i] * b[i])

print("Dot Product:",dot_product)