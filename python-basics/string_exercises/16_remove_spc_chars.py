#Remove special symbols / punctuation from a string

import string
def rmv_spc_chars(str1):
    x = '@#$%^&*>'
    y = ''
    mytable = str.maketrans("x", "y")
    print(str1.translate(str.maketrans('', '', string.punctuation)))


str1 = "/*Jon is @developer & musician"
rmv_spc_chars(str1)