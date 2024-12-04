# Make a two-player Rock-Paper-Scissors game.


def first_user_input():

    ans_1 = False
    while ans_1 == False:
        first_user_input = input("Player 1 enter your Choice (Rock,Paper,Scissors) : ")
        if first_user_input.lower() == "rock" or first_user_input.lower() == "paper" or  first_user_input.lower() == "scissors":
            ans_1 = True
            return first_user_input
        else:
            print("Incorrect Choice. You need to enter between rock, paper or scissors")

def second_user_input():
    ans_2 = False
    while ans_2 == False:
        second_user_input = input("Player2 enter your Choice (Rock,Paper,Scissors) : ")
        if second_user_input.lower() == "rock" or second_user_input.lower() == "paper" or  second_user_input.lower() == "scissors":
            ans_2 = True
            return second_user_input
        else:
            print("Incorrect Choice. You need to enter between rock, paper or scissors")

def comparison(first_user_input, second_user_input):
    if (first_user_input == "rock" and second_user_input == "scissors") or (first_user_input == "scissors" and second_user_input == "paper") or (first_user_input == "paper" and second_user_input == "rock"):
        print(first_user_input, "beats", second_user_input, "Player 1 has won")
    elif (first_user_input == "scissors" and second_user_input == "rock") or (first_user_input == "paper" and second_user_input == "scissors") or (first_user_input == "rock" and second_user_input == "paper"):
        print(second_user_input, "beats", first_user_input, "Player 2 has won")
    elif first_user_input == second_user_input:
        print("Its a tie")

def main():


    ans_3 = False
    while ans_3 == False:
        first_user = first_user_input()
        second_user = second_user_input()
        comparison(first_user, second_user)
        ans_4 = input("want to start a new game (Y/N)? ")
        if ans_4.lower() == 'n':
            ans_3 = True


main()






    





