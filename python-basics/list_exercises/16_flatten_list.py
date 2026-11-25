# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).


def flatten_list(list1):
    new_list = []
    for i in list1:
        for j in i:
            new_list.append(j)
    print(new_list)


list1 = [[1, 2], [3, 4], [5, 6, 7]]

flatten_list(list1)