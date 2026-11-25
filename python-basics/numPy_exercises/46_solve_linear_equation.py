# Exercise 46: Solve a linear equation

#Solve the system of linear equations: x + 2y = 8 and 3x + 4y = 18.


import numpy as np

# Define the coefficient matrix A
A = np.array([[1, 2], [3, 4]])

# Define the right-hand side vector b
b = np.array([8, 18])

# Solve for x and y
solution = np.linalg.solve(A, b)
print(solution)