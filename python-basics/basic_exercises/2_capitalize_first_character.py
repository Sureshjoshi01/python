#Capitalize the first letter of each word in a string

import string

def capitalize_first_character(str):
    capitalized_words = []
    words = str.split()
    for i in words:
        capitalized_words.append(i.capitalize())
    return " ".join(capitalized_words) 


str = input("Enter String : ")
str = capitalize_first_character(str)
print(str)




