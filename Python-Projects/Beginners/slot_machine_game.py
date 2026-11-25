# Slot Machine Game
# The Slot Machine Game is a fun and simple project that simulates a classic slot
# machine. The player starts with a balance, places bets, and spins the reels. If the
# symbols on the reels match, the player wins a payout based on their bet. The
# game continues until the player either runs out of money or decides to walk away
# with their winnings.
# Payout Rules:
# • If all three symbols match, the player wins 10 times their bet.
# • If two out of three symbols match, the player wins 2 times their bet.
# • If none of the symbols match, the player loses their bet.

import random
symbols = ["🍒", "⭐", "🍋", "🔔", "💎"]


def starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance : $"))
            if balance <=0:
                print("Enter a number greater then 0")
                continue
            break  
        except ValueError:
            print("You need to enter numbers only") 
    return balance


def spin_machine(balance):
    print(f"Current balance: ${balance}")
    while True:
        try:
            bet = int(input("Enter your bet amount : $"))
            if bet > balance:
                print("Insufficient balance")
                continue
                
            if bet <=0:
                print("Enter a number greater then 0")
                continue
            break  
        except ValueError:
            print("You need to enter numbers only") 


    spin = random.choices(symbols,k=3)
    return bet,spin  
    
def slot_machine():
    
    balance = starting_balance()
    print()
    print("Welcome to the Slot Machine Game!")
    print(f"You start with a balance of ${balance}")
    print()
    while True:
        winning_amount = 0
        bet,spin = spin_machine(balance) 
        print(" | ".join(spin))
                    balance = balance - bet
        if spin[0] == spin[1] == spin[2]:
            winning_amount = 10 * bet
            balance = winning_amount + balance
        elif spin[0] == spin[1] or spin[1] == spin[2] or spin[2] == spin[0]:
            winning_amount = 2 * bet 
            balance = winning_amount + balance
        else:
            print("You lost the bet")
        
        print(f"You won ${winning_amount}")
        print(f"New balance: ${balance}")

        if balance <= 0:
            print("Game Over")
            break

        while True:
            answer = input("Do you want to play again (y/n)? ").strip().lower()
            if answer in ("y", "n"):
                break
            print("Please enter Y or N.")
        if answer == "n":
            break
        

slot_machine()
