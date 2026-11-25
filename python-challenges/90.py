# Question 90

# By using list comprehension, 
# please write a program generate a 358 3D array whose each element is 0.

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)