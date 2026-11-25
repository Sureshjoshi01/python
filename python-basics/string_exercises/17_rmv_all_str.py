# Removal all characters from a string except integers
 
def rmv_all_char(str1):
    str2 = ''
    for i in str1:
        if i.isdigit():
            str2 = str2 + i
    print(str2) 



str1 = 'I am 25 years and 10 months old'
rmv_all_char(str1)