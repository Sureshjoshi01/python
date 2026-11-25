# Write a program to create a new string made of the middle three characters of an input string.

def str_frm_mid_three_char(str1):
    l = int(len(str1)/2) - 1
    str1 = str1[l] + str1[l+1] + str1[l+2]
    return str1




str1 = "JhonDipPeta"
str2 = "JaSonAy"
print(str_frm_mid_three_char(str1))
print(str_frm_mid_three_char(str2))