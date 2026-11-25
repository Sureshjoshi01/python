#Write a Python program to print the reverse number pattern using a for loop.

#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1
num = 5
for i in range(1,6):
    for j in range(num,0,-1):
        print(j,end="")
    num = num - 1
    print()
