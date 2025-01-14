#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def rand_num():
    num = random.randint(1,9)
    return num

def user_number():
    user_input = int(input("Enter a number between 1 and 9 : "))
    lst = [1,2,3,4,5,6,7,8,9]
    ans = True
    while ans == True:

        if user_input not in lst:
            user_input = int(input("You need to enter number between 1 and 9 or enter 0 to exit program: "))
            if user_input == 0:
                exit("You Choose to close the game")
        else:
            ans =  False
    return user_input

def guess(num):
    user_input = user_number()
    print(num)
    ans = True
    while ans == True:
        if user_input == num:
            print("You have guessed the right number")
            ans = False
        elif user_input > num:
            print("You have guessed too high")
            num = user_number()
        else:
            print("You have guessed too low")
            num = user_number()


def main():

    num = rand_num()
    guess(num)
       

main()




