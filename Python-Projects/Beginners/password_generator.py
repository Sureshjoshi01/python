# # Write a program to generate a random password based on user-specified criteria,
# # such as length, and whether to include uppercase letters, numbers, and special
# # characters.
# # Optional Enhancements
# Modify the program so the user can specify how many passwords they want
# to generate at one time. The program should then create and display all the
# passwords.
# Add an option to save the generated passwords to a text file. This allows
# users to keep a record of their passwords for future reference.

import random
import os
from pathlib import Path

small_letters      = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
capital_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers            = ['0','1','2','3','4','5','6','7','8','9']
special_character  = ['@','#','!','%','&','?','$','^']
allowed_characters = []
passwords = []

while True:
    try:
        n = int(input("Enter Number of passwords required : "))
        if n < 1:
            print("Number must be greater than 0")
            continue
        break
    except ValueError:
        print("Only integers are allowed")

for i in range(n):
    passwd = []
    passwd = passwd + random.choices(small_letters)
    while True:
        try:
            length = int(input("Enter Password Length: "))
            if length < 1:
                print("Length must be greater than 0")
                continue
            break
        except ValueError:
            print("Only integers are allowed")

    while True:
        print("Include Upper Case letter (y/n) or (Y/N) ? ",end="")
        cap_char = input().lower()
        if cap_char == 'y' or cap_char == 'n' :
            break
        else:
            print("Only Y/N or y/n are allowed")

    while True:
        print("Include numbers (y/n) or (Y/N)? ",end="")
        num = input().lower()
        if num == 'y' or num == 'n':
            break
        else:
            print("Only Y/N or y/n are allowed")  

    while True:
        print("Include special characters (y/n) or (Y/N)? ",end="")
        spc_ch = input().lower()
        if spc_ch == 'y' or  spc_ch == 'n':
            break
        else:
            print("Only Y/N or y/n are allowed")     

    
    allowed_characters = small_letters.copy()
    if cap_char == 'y':
        allowed_characters += capital_characters
        passwd = passwd + random.choices(capital_characters)
    if num == 'y':
        allowed_characters += numbers
        passwd = passwd + random.choices(numbers)
    if spc_ch == 'y':
        allowed_characters += special_character
        passwd = passwd + random.choices(special_character)

    rem = length - len(passwd)

    passwd = passwd + random.choices(allowed_characters,k=rem)
    passwords.append(passwd)

list_of_passwords = []
for i in passwords:
    random.shuffle(i)
    list_of_passwords.append((''.join(i)))




f = open("passwords.txt","w")
for i in list_of_passwords:
    f.write(i)
    f.write("\n")
f.close()