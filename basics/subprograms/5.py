
import csv

def add():
    file =  open("Salaries.csv","a")
    name = input("Enter your name : ")
    salary = int(input("Enter your salary : "))
    newRecord = name + "," + str(salary) + "\n"
    file.write(newRecord)
    file.close()

def view():
    file = open("Salaries.csv","r")
    for row in file:
        print(row)


def main():   
    ans = 'y'
    while ans == 'y':
        print(" 1) Add to file : ")
        print(" 2) View all records : ")
        print(" 3) Quit Program : ")
        selection = int(input("Enter the number of your selection : "))
        if selection == 1:
            add()
        elif selection == 2:
            view()
        elif selection == 3:
            print("Quiting Program")
            ans = 'n'
        else:
            print("Wrong Choice, make selection again")


main()

