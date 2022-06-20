import random

colors = ["red","pink","blue","green","black","white","yellow","brown"]


def comp_list():
    comp_list = []
    for i in range(0,4):
        choice = random.choice(colors)
        comp_list.append(choice)
    #print(comp_list)
    return comp_list

    
def check(comp_list):
    print(comp_list)
    user_list = []
    print("Enter 4 colors from below list : ")
    print(colors)
    for i in range(1,5):
        print("Enter ",i," Color :",end=" ")
        choice = input()
        choice = choice.lower()
        ans = True
        while ans == True:
            if choice not in colors:
             print(" This color is not availaible for selection, select from : ",colors)
             choice = input("Enter again : ")
             choice = choice.lower()
            else:
                ans = False
        user_list.append(choice)              
    
    

    
    
    print(user_list)
    correct = 0
    wrong_place = 0
    
    if comp_list[0] == user_list[0]:
        correct = correct + 1
    elif comp_list[0] == user_list[1] or comp_list[0] == user_list[2] or comp_list[0] == user_list[3]:
        wrong_place = wrong_place + 1
    
    if comp_list[1] == user_list[1]:
        correct = correct + 1
    elif comp_list[1] == user_list[0] or comp_list[1] == user_list[2] or comp_list[1] == user_list[3]:
        wrong_place = wrong_place + 1

    if comp_list[2] == user_list[2]:
        correct = correct + 1
    elif comp_list[2] == user_list[0] or comp_list[2] == user_list[1] or comp_list[2] == user_list[3]:
        wrong_place = wrong_place + 1

    if comp_list[3] == user_list[3]:
        correct = correct + 1
    elif comp_list[3] == user_list[0] or comp_list[3] == user_list[1] or comp_list[3] == user_list[2]:
        wrong_place = wrong_place + 1

    print("Correct Color in Correct place : ",correct)
    print("Correct color but in the wrong place : ",wrong_place)
    print()
    data2 = [correct, wrong_place]
    return data2
    
                
            

def main():
    a = []
    a = comp_list()
    score = 0
    play = True
    while play == True:
        (correct,wrong_plce) = check(a)
        score = score + 1
        if correct == 4:
            play= False
    print("You win") 
    print("You took", score,"guesses")


main()


        



