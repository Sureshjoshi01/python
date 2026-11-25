#Write a program to print the following start pattern using the for loop.

#* 
#* * 
#* * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*

def star_pattern():
    num = 4
    for i in range(0,5):
        for j in range(i+1):
            print("*",end=" ")
        print()
    for i in range(0,4):
        for j in range(num,0,-1):
            print("*",end=" ")
        num = num - 1
        print()
star_pattern()
