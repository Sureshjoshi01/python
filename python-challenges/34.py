# Question 34

# Define a function which can print a dictionary where the keys are numbers 
# between 1 and 20 (both included) and the values are square of keys.

def print_dict():
    dict = {}
    for i in range(1,21):
        dict[i] = i*i
    print(dict)

print_dict()
