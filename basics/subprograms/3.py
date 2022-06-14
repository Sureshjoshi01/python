import random

def addition():
    n1 = random.randint(5,20)
    n2 = random.randint(5,20)

    print(n1 , "+" , n2, "=",end=" ")
    user_input = int(input())
    ans = n1 + n2
    ans_list = (user_input,ans)
    return ans_list

def subtraction():
    n1 = random.randint(25,50)
    n2 = random.randint(1,25)

    print(n1 , "-" , n2, "=",end=" ")
    user_input = int(input())
    ans = n1 - n2
    ans_list = (user_input,ans)
    return ans_list


def check(user_input,ans):
    if user_input == ans:
        print("Correct")
    else:
        print("Incorrect, the answer is : ",ans)

def main():
    print(" 1) Addition ")
    print(" 2) Subtraction ")
    choice = int(input("Enter 1 or 2 : "))
    if choice == 1:
        user_input,ans = addition()
        check(user_input,ans)
    elif choice == 2:
        user_input,ans = subtraction()
        check(user_input,ans)
    else: 
        print("Wrong Choice , Please select either 1 or 2")

main()



   

    

