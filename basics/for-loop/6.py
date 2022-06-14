n = int(input("Enter a number below 50 : "))
if n>50: 
    print("Number must be smaller than 50 ")
    exit
else:
    for i in range(50,n,-1):
        print(i)
    
     