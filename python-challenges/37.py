# Question 37

# Define a function which can generate and 
# print a list where the values are square of numbers between 1 and 20 (both included).

def generate_lst():
    lst = []
    for i in range(1,21):
        lst.append(i*i)
    print(lst)

generate_lst() 
