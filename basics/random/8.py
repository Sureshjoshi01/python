import random

choice = random.choice(['Red','Pink','Yellow','Green','Black'])
print ("/n ***** colors *****")
print("\nRed\nPink\nYellow\nGreen\nBlack")

guess = False
while guess != True: 
    str = input("Pick a color from above list : ") 
    if str.upper() != choice.upper():
        print("You are probably feeling ",choice,"now")
    else:
        print("Well Done")
        guess = True
