# Number Guessing Game 

import random
def number_guess():
    random_number = random.randint(1,10)
    print("Welcome to the Number Guessing Game!")
    
    while True:
        try:
            print("Guess a number between 1 and 10 : ",end="")
            user_input = int(input())


            if user_input < 1 or user_input > 10:
                print("Out of range! Please pick a number from 1 to 10.")
                continue

        except ValueError:
            print("You need to enter an integer between 1 and 10")
            continue
  
        if user_input == random_number:
            print("Wow! you have selected the right number ",random_number)
            break
        elif user_input > random_number:
            print("You have guessed number greater than the target")
        elif user_input < random_number:
            print("You have guessed number smaller than the  target")
  


number_guess()





