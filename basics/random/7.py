import random
print("\n ********** Maths Quiz *********** \n")


score = 0
for i in range(1,6):
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    choice = random.choice(['+','-','*','/','%'])
    print("What is ",num1,choice,num2,"?")
    ans = int(input())
    if num1+num2 == ans:
        score = score+1
    elif num1-num2 == ans:
        score = score+1
    elif num1*num2 == ans:
        score = score+1
    elif int(num1/num2) == ans:
        score = score+1
    elif int(num1%num2) == ans:
        score = score+1

print("\nYour score is :", score)

