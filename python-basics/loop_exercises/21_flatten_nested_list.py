# Flatten a nested list using loops



def flattten_list(nested_list):
    flat_list = []
    reversed_list = []
    for i in range(len(nested_list)):
        n = nested_list.pop()
        reversed_list.append(n)

    for j in range(len(reversed_list)):
        current = reversed_list.pop()
        if type(current) == list:
            for i in current:
                flat_list.append(i)
        else:
            flat_list.append(current)
    return flat_list 

nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
flattened = flattten_list(nested_list)
print("Flattened list:", flattened)
