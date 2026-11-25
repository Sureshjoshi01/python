# ROCK PAPER SCISSORS GAME 

import random

def rock_paper_scissors_game():

    ch = ["ROCK","PAPER","SCISSORS"]
    computer_choice = random.choice(ch)
    
    while True:

            print("Enter your choice from ROCK,PAPER,SCISSORS : ",end="")
            user_choice = input().upper()

            if user_choice in ch:
                break

            if user_choice not in ch:
                print("You need to enter choice from ROCK,PAPER,SCISSORS")
                continue

    print("Computer Selection - ",computer_choice)
    print("User Selection - ",user_choice)
    if user_choice.upper() == "ROCK" and computer_choice == "SCISSORS":
        return "You Win"
    elif  user_choice.upper() == "ROCK" and computer_choice == "PAPER":
        return "You Loose! Computer wins"
    elif  user_choice.upper() == "ROCK" and computer_choice == "ROCK":
            return "Its A Tie"
    elif  user_choice.upper() == "PAPER" and computer_choice == "SCISSORS":
        return "You Loose! Computer wins"
    elif  user_choice.upper() == "PAPER" and computer_choice == "ROCK":
        return "You Win"
    elif  user_choice.upper() == "PAPER" and computer_choice == "PAPER":
        return "Its A Tie"
    elif  user_choice.upper() == "SCISSORS" and computer_choice == "PAPER":
        return "You Win"
    elif  user_choice.upper() == "SCISSORS" and computer_choice == "ROCK":
        return "You Loose! Computer wins"
    elif  user_choice.upper() == "SCISSORS" and computer_choice == "SCISSORS":
        return "Its A Tie"
    

result = rock_paper_scissors_game()
print(result)
