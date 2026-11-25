# The Cows and Bulls Game is a fun number-guessing challenge that tests your
# logical thinking and problem-solving skills. In this project, you’ll build a game
# where the computer comes up with a secret 4-digit number, and your job is to
# guess it. After each guess, you’ll get feedback in the form of "cows" and "bulls"—
# a "bull" means you’ve guessed the right digit in the right spot, while a "cow"
# means the digit is correct but in the wrong spot.

# Optional Enhancements
# • Allow the player to choose a difficulty level at the start of the game, which
# changes the length of the secret number or the number of attempts allowed.

import random
number_list = ['0','1','2','3','4','5','6','7','8','9']

def generate_number(no_of_digit):    
    number = random.sample(number_list,k=no_of_digit)
    return number

def guess_number(no_of_digit,no_of_attempts):
    count = 0
    number = generate_number(no_of_digit)
    print(number)
    print(f"I have generated a {no_of_digit}-digit number with unique digits. Try to guess it!")
    while True:
        lst = []
        cows = 0
        bulls = 0
        Guess = input("Guess: ")
        if not Guess.isdigit():
            print("Only digits are allowed")
            continue
        if len(str(Guess)) != no_of_digit:
            print(f"Enter exactly {no_of_digit} digits")
            continue
        if len(set(Guess)) != no_of_digit:
            print("Digits must be unique")
            continue
        for i in str(Guess):
            lst.append(i)
        print(lst)
        
        if lst == number:
            print("Correct Guess")
            return
        else:
            for i in range(no_of_digit):
                if lst[i] == number[i]:
                        bulls +=  1
                elif lst[i] in number:
                    cows +=  1
            print(f"{cows} cows, {bulls} bulls")
        count += 1
        if count == no_of_attempts:
            print("Attempts Exhausted!")
            print("The correct number was:", "".join(number))
            return
        remaining = no_of_attempts - count
        print(f"Attempts remaining: {remaining}")


def main():
    print("****** Cows and Bulls Game ******")
    print("Choose the difficulty level - ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard" )
    print("Easy   - Only 3 digit number and 10 attempts for guessing.")
    print("Medium - 4 digit numbers and 8 attempts for guessing.")
    print("Hard   - 6 digit number and 6 attempts for guessing.")
    print("Difficulty Level : ",end="")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("Please enter a valid choice i.e 1,2 or 3")
            continue
        if choice not in [1,2,3]:
            print("Please enter a valid choice i.e 1,2 or 3")
        else:
            break

    if choice == 1:
        guess_number(3,10)
    elif choice == 2:
        guess_number(4,8)
    elif choice == 3:
        guess_number(6,6)

main()