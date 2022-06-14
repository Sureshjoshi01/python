import random

def gen_num():
    low = int(input("Enter a number which should act as lower : "))
    high = int(input("Enter a number which should act as high : "))
    comp_num = random.randint(low,high)
    return comp_num

def guess():
    print("I am thinking of a number : ")
    num = int(input(" Guess number i am thinking of : "))
    return num

def check_num(comp_num,num):
    ans = 'n'
    while ans == 'n':
        if comp_num == num: 
            print("Correct, You win")
            ans = 'y'
        elif num > comp_num: 
            num = int(input(" Too high, try again  : "))
        elif num < comp_num:
            num = int(input(" too low , try again : "))
def main():
    x = gen_num()
    y = guess()
    check_num(x,y)

main()


