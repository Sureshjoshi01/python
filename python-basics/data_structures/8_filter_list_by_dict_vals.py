# Write a program to iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list


roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number_new = []

for i in roll_number:
    for v in sample_dict:
        if i == sample_dict[v]:
            roll_number_new.append(i)


print("After removing unwanted elements from list", roll_number_new)