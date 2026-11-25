# Given string contains a combination of the lower and upper case letters. 
# Write a program to arrange the characters of a string so that all lowercase letters should come first.

def arrange_string(str1):
    s1 = ""
    s2 = ""
    for i in str1:
        if i.islower():
            s1 = s1 + i
        else:
            s2 = s2 + i
    s3 = s1 + s2
    return s3


str1 = "PyNaTive"
str2 = "SuReShJoShI"
print(arrange_string(str1))
print(arrange_string(str2))