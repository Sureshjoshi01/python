# Find the largest item from list


def larger_in_lst(lst):
    large = 0
    for i in lst:
        if i > large:
            large = i
    return large

x = [4, 6, 8, 24, 12, 2]
print(larger_in_lst(x))
print(max(x))


