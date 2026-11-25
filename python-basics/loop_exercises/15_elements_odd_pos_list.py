# Print elements from a given list present at odd index positions

def odd_index(my_list):
    for i in range(len(my_list)):
        if i % 2 != 0:
            print(my_list[i])


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

odd_index(my_list)