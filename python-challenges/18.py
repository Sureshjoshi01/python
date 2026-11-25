# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
cap_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
small_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","m","o","p","q","r","s","t","u","v","w","x","y","Z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
special_char = ["$","#","@"]
passwd= []
passwords = input()
passwd = passwords.split(",")
print(passwd)

for i in passwd:
    if len(i) < 6 or len(i) > 12:
        continue
    A1 = False  
    A2 = False  
    A3 = False  
    A4 = False
    for j in i:
        if j in cap_alphabets:
            A1 = True
        elif j in small_alphabets:
            A2 = True
        elif j in num:
            A3 = True
        elif j in special_char:
            A4 = True

    if A1 and A2 and A3 and A4:
        print(i,end=",") 