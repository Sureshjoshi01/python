#Exercise 45: Compute the eigenvalues and eigenvectors of a matrix

#For a square matrix, compute its eigenvalues and eigenvectors.

import numpy as np
A = np.array([[4, 2],
              [1, 3]])


eigen_values , eigen_vectors = np.linalg.eig(A)

print(eigen_values)
print(eigen_vectors)

