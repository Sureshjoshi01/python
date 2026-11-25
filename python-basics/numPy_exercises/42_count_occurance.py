# Exercise 42: Count the number of occurrences of each unique element


import numpy as np
arr = np.array([2, 3, 2, 5, 3, 3, 2, 5])


count = 0 
for i in arr:
    if int(i) == 2:
        count= count + 1

print("Value 2 occurs", count ,"time(s)")

vals, counts = np.unique(arr, return_counts=True)
for v, c in zip(vals, counts):
    print(f"Value {v} occurs {c} time(s)")