#Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False

def check(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False
    
print(check([10, 20, 30, 40, 10]))
print(check([75, 65, 35, 75, 30]))
    


    