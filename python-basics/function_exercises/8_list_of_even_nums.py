# Generate a Python list of all the even numbers between 4 to 30

def list_of_even_nums():
    lst = []
    for i in range(3,30):
        if i % 2 == 0:
            lst.append(i)
    return lst


print(list_of_even_nums())