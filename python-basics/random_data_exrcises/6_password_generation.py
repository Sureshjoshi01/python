# Write a code to generate a random password which meets the following conditions.

#    Password length must be 10 characters long.
#    It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.


import string
import random


characters = string.ascii_uppercase + string.digits + string.punctuation
password  = random.sample(characters, k=6)
password += random.sample(string.ascii_uppercase,k=2)
password += random.choice(string.digits)
password += random.choice(string.punctuation)
print(characters)
print(password)
passwordList = list(password)
random.SystemRandom().shuffle(passwordList)
password = ''.join(passwordList)

print(passwordList)
print(password)

