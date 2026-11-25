# The Pig Dice Game is a fun, strategic game where two players compete to be the
# first to reach 100 points. In this project, you’ll build a simplified version of the
# game where each player rolls a die repeatedly to accumulate points. However, if
# they roll a 1, they lose all points accumulated in that turn and must pass the die to
# the other player. The game requires players to decide whether to keep rolling to
# increase their score or to hold and secure their points before risking a roll of 1.


import random
    
def turns():
    n = random.randint(1,6)
    return n

def player_turn(player_name, total_score):
    turn_score = 0

    print(f"{player_name}'s turn")

    while True:
        n = turns()
        print(f"You rolled a {n}")

        if n == 1:
            print("You Scored 0 points this turn")
            return total_score

        turn_score += n

        print("Roll again ? (y/n) : ", end="")

        while True:
            ans = input().lower()

            if ans not in ['y', 'n']:
                print("Only y and n is allowed")
            else:
                break

        if ans == 'n':
            total_score += turn_score

            print(f"You Scored {turn_score} points this turn")
            print(f"Total Score: {total_score}")

            return total_score
def main():
    player1_score = 0
    player2_score = 0

    print("****** Pig Dice Game *****")
    print()

    while True:

        player1_score = player_turn("Player 1", player1_score)

        print()

        player2_score = player_turn("Player 2", player2_score)

        print()

        if player1_score >= 100:
            print("Player 1 wins")
            break

        elif player2_score >= 100:
            print("Player 2 wins")
            break

main()
