# Reverse a given string


def reverse_str1(str1):
    str2 = str1[::-1]
    print(str2)


str1 = "PYnative"
reverse_str1(str1)

def reverse_str1(str1):
    lst = []
    str2 = ''
    for i in str1:
        lst.append(i)
    while len(lst) != 0:
        str2 = str2 + lst.pop()
    print(str2)



str1 = "PYnative"
reverse_str1(str1)