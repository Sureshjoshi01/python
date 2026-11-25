#Check if a user-entered string contains any digits using a for loop


def check_string_for_digit(str):
    contains_num = False
    for i in str:
        if ((i=='0') or (i=='1') or (i=='2') or (i=='3') or (i=='4') or (i=='5') or (i=='6') or (i=='7') or (i=='8') or (i=='9')):
            contains_num = True
    return contains_num
              

str = input("Enter string : ")            
if(check_string_for_digit(str) == True):
    print("The string contains at least one digit.")
else:
    print("The string does not contain any digits.")