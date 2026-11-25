# Write a program to split a given string on hyphens and display each substring.


def split_string(str1):
    str2 = str1.split('-')
    for i in str2:
        print(i)
str1 = 'Emma-is-a-data-scientist'
split_string(str1)
