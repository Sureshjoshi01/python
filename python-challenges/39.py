# Question 39

# Define a function which can generate a list where the values are square of numbers between 
# 1 and 20 (both included). 
# Then the function needs to print the last 5 elements in the list.
def generate_lst():
    lst = []
    for i in range(1,21):
        lst.append(i*i)
    print(lst[-5:])

generate_lst() 