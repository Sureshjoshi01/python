# Stack arrays horizontally

import numpy as np 

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

new_array = np.hstack((a,b)) 
 # second () needed This is needed because np.hstack’s 
 # signature is: np.hstack(tup), where tup is a tuple of arrays.
 # The outermost parentheses call the function.
# The innermost parentheses create a tuple.
print(new_array)