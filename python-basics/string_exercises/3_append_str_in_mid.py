# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

def append_in_middle(s1,s2):
    l = int(len(s1)/2)
    s3 = s1[0:l] + s2 + s1[l:]
    print(s3)





s1 = "Ault"
s2 = "Kelly"
append_in_middle(s1,s2)