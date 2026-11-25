# Given a tuple of numbers, create a new tuple where each number is squared.


#map()
t = (1, 2, 3, 4)
print(f"Original tuple: {t}") 

# First Method
t = (1, 2, 3, 4)
squared_tuple = []
for i in t:
  squared_tuple.append(i * i)

print(tuple(squared_tuple))
squared_tuple_map = tuple(map(lambda x: x**2, t))
print(f"Squared tuple (map function): {squared_tuple_map}")