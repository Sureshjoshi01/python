#Use a lambda with the map() function to double each element in a list

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(lambda x: x+x,numbers))
print("The doubled numbers are:",doubled_numbers)