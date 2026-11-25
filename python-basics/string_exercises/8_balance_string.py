# Write a program to check if two strings are balanced. 
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
# The character’s position doesn’t matter.

def check_balance_str(s1,s2):
    l = len(s1)
    flag = True
    for i in s1:
        if i in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
result = check_balance_str(s1,s2)
if result == True:
        print(s1,s2,"are balanced string")
else:
        print(s1,s2,"are not balanced string")

s1 = "Ynf"
s2 = "PYnative"
result = check_balance_str(s1,s2)
if result == True:
        print(s1,s2,"are balanced string")
else:
        print(s1,s2,"are not balanced string")

s1 = "joshi"
s2 = "sureshjoshi"
result = check_balance_str(s1,s2)
if result == True:
        print(s1,s2,"are balanced string")
else:
        print(s1,s2,"are not balanced string")
