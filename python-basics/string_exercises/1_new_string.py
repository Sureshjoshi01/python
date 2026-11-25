# Write a program to create a new string made of an input string’s first, middle, and last character.

def new_string(str1):
    n = int(len(str1)/2)
    str1 = str1[0] + str1[n] + str1[-1]
    return str1




str1 = "James"
str2 = "Suresh"
print(new_string(str1))
print(new_string(str2))
