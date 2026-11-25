# Password Strength Checker
# Write a program to evaluate the strength of a password based on criteria like
# length, the inclusion of uppercase letters, numbers, and special characters. The
# program will then categorize the password as Very Weak, Weak, Medium, Strong,
# or Very Strong.
# Optional Enhancements
# After evaluating the password, give the user suggestions on how to make it
# stronger, such as adding more characters, including special symbols, or
# avoiding common words.
# Copyright

     
def capital_letter_check(passwd):
    capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    found = False
    cap = 0
    for i in passwd:
        for j in capital_letters:
                if i == j:
                    found = True
                    cap = cap + 1
                    break
        if found:
             break
    return cap 

def small_letter_check(passwd):
    small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    found = False
    sml = 0
    for i in passwd:
        for j in small_letters:
                if i == j:
                    found = True
                    sml = sml + 1
                    break
        if found:
             break
    return sml

def numbers_check(passwd):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    found = False
    num = 0
    for i in passwd:
        for j in numbers:
            if i == j:
                 found = True
                 num = num + 1
                 break
        if found:
             break
    return num
        
def special_symbol_check(passwd):
    special_symbols = ['@','#','!','%','&','?','$','^']
    found = False
    ch = None
    spc= 0
    for i in special_symbols:
        for j in passwd:
            if i == j:
                found = True
                ch = j
                spc = spc + 1
                break
        if found:
            break
    return spc
    
def main():
    score = 0
    l = 0

    print("Enter Password : ",end="")
    passwd = input()
    if len(passwd) > 6:
        l = l + 1 

    
    score  = capital_letter_check(passwd) + small_letter_check(passwd) + numbers_check(passwd) + special_symbol_check(passwd) + l

    if score == 5:
        print("Very Strong")
    if score == 4: 
        print("Strong")
    if score == 3: 
         print("Medium")    
    if score == 2: 
        print("Weak")
    if score == 1: 
        print("Very Weak")

    if capital_letter_check(passwd) == 0:
        print("Use atleast one Capital letter to make password more strong")
    if small_letter_check(passwd) == 0: 
        print("Use atleast one Small letter to make password more strong")
    if numbers_check(passwd) == 0: 
         print("Use atleast one number to make password more strong")    
    if special_symbol_check(passwd) == 0: 
        print("Use atleast Special Symbol from '@','#','!','%','&','?','$','^' to make password more strong")
main()

 

      




