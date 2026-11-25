# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

sorted_list_of_tuples = sorted(my_dict.items(), key=lambda item: item[1])
print(sorted_list_of_tuples)