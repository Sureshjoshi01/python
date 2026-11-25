# Question 36

# Define a function which can generate a 
# dictionary where the keys are numbers between 1 
# and 20 (both included) and the values are square of keys. 
# The function should just print the keys only.

def print_dict():
    dict = {}
    for i in range(1,21):
        dict[i] = i*i
    for k,v in dict.items():
        print(k)

print_dict()