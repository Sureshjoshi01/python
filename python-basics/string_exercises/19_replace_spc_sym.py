# Replace each special symbol with # in the following string
import string
str1 = '/*Jon is @developer & musician!!'

replace_char = '#'
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print(str1)