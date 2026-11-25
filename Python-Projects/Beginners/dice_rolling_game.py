# # Write a program that simulates rolling a pair of dice. Each time the program runs, it
# should randomly generate two numbers between 1 and 6 (inclusive), representing
# the result of each die. The program should then display the results and ask if the
# user would like to roll again.

import random 

def dice_rolling():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1,dice2


while True:
    print("Roll the dice ? (y/n? ",end="")
    ans = input()
    if ans == "n":
        break
    else:
        a,b = dice_rolling()
        print(a,b)
    

