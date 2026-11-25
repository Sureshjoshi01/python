# Exercise 19: Perform arithmetic operations on two NumPy arrays element-wise

#    Add two NumPy arrays element by element.
#    Multiply two NumPy arrays element by element.


import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.add(a,b)
d = np.multiply(a,b)


print("Element-wise Sum:", c)
print("Element-wise multiplication:", d)
