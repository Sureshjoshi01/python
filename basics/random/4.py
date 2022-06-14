from random import random


import random
num = random.randint(1,5)
num2 = int(input("Enter a number : " ))
if num2 == num:
    print("Well Done")
elif num2 > num:  
    print("Too High")
    num3 = int(input("Enter another number : " ))
    if num3 == num :
        print("Correct")
    else: 
        print("You Lose")
        
elif num2 < num:
    print("Too Low")
    num3 = int(input("Enter another number : " ))
    if num3 == num:
        print("Correct")
    else: 
        print("You Lose")

