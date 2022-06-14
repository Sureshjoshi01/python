word = input("Enter a word in upper case : ")
ans = 'n'
while ans == 'n':
    if word.upper() != word:
        print("Try Again") 
        word = input("Enter a word in upper case : ")
    else:
        ans = 'y'


    
 