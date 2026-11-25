# Write a code to generate random string of length 5.

import string
import random

def get_random_string(length):
    result = ''
    letters = string.ascii_letters
    for i in range(length):
        result= result + random.choice(letters)
    return result

print ("Random String is ", get_random_string(5) )


