#Print Array Attributes

#Instructions: Print the following attributes of the array:

#    The shape of the array.
#    The number of array dimensions.
#    The size of each element in bytes.


import numpy as np
my_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)

print("The shape of the array is: ",my_array.shape)
print("The number of dimensions is: ",my_array.ndim )
print("The size of each element in bytes is: ", my_array.itemsize) 