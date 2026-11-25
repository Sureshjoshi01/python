# Quiz Game
# Write a program to create a quiz where the player answers multiple-choice
# questions. The program should evaluate the player's answers and provide a score
# at the end.
# Optional Enhancements
# • Allow the player to choose from different categories of questions, such as
# history, science, or geography.
# • Implement different difficulty levels by varying the complexity of the
# questions.
# • Modify the game to import questions from a CSV or JSON file, allowing for
# easy updates and additions to the quiz content.
import csv 
from pathlib import Path

def subject_selection():
    while True:
        print("Choose Subject?")
        print("a) History b) Science c) Geography")
        user_input = input().lower()
        if user_input not in ['a','b','c']:
            print("Wrong Selection")
        else:
            if user_input == 'a':
                return "History"
            elif user_input == 'b':
                return "Science"
            else:
                return "Geography"

def category_selection():
    sub = subject_selection()
    while True:
        print("Select Category?")
        print("a) Easy b) Hard")
        user_input = input().lower()
        if user_input not in ['a','b']:
            print("Wrong Selection")
        else:
            if sub =="History" and user_input == "a":
                return "quiz_questions/history_easy.csv"
            elif sub =="History" and user_input == "b":
                return "quiz_questions/history_hard.csv"
            elif sub =="Science" and user_input == "a":
                return "quiz_questions/science_easy.csv"
            elif sub =="Science" and user_input == "b":
                return "quiz_questions/science_hard.csv"
            elif sub =="Geography" and user_input == "a":
                return "quiz_questions/geography_easy.csv"
            elif sub =="Geography" and user_input == "b":
                return "quiz_questions/geography_hard.csv"

def ques_ans():
    while True:
        filename = category_selection()
        file_path = Path(filename)
        if file_path.is_file(filename):
            with open(filename,"r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                if rows == []:
                    print(f"the file {filename} contains no questions")
                    continue
                else:
                    break
        else:
            print(f"Error: The file {filename} does not exist in this location.")
            continue
    ans = rows.pop()
    return rows,ans

def quiz():
    ques,ans = ques_ans()
    score = 0
    j = 0
    for question in ques:
        for option in question:
            print(option)
        while True:
            answer = input("Your answer: ").lower()
            if answer not in ['a','b','c','d']:
                print("Wrong Selection, you need to select from a,b,c,d options")
            elif answer == ans[j]:
                print("Correct!")
                score = score + 1
                break
            else:
                print("Not Correct!")
                print(f"Correct answer was ",ans[j])
                break
        j = j + 1
    print(f"Your final Score: {score}/{len(ans)}")

    


def main():
    print ("**********************QUIZ GAME************************")
    print()
    quiz()
    while True:
        print("Play again? (Y/N)")
        user_ans = input().upper()
        if user_ans not in ['Y','N']:
            print("Wrong Selection, you need to select from Y/N options")
        else: 
            if user_ans == 'Y':
                quiz()
            else:
                break

    
main()


