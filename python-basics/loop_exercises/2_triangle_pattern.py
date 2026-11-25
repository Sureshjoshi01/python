#Write a Python code to print the following number pattern using a loop.
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5


for i in range(0,5):
    for j in range(0,i+1):
        print(i+1,end="")
    print("")
        