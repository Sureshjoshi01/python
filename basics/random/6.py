import random
num = random.randint(1,10)
correct = False
while correct == False: 
    num2 = int(input("Enter a number : "))
    if num2 == num:
        correct = True
    elif num2 > num: 
        print("Too High")
    else:
        print("Too Low")

