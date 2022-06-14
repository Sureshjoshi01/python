import random
num = random.randint(1,10)
num2 = int(input("Enter a number : "))
while num2 != num: 
    num2 = int(input("Enter a number : "))
print(num)
print(num2)