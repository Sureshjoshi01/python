# Exercise 23: Normalize a NumPy array (values between 0 and 1)

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized Array:", normalized)

