
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
    file.close()

def delete():
    file = open("Salaries.csv","r")
    tmp = []
    for row in file: 
        tmp.append(row)
    file.close()

    x = 0
    for i in tmp:
        print(x,i)
        x = x+1

    dele = int(input("Enter row number to delete that row : "))
    del tmp[dele] 
    
    file = open("Salaries.csv","w")

    for row in tmp:
        file.write(row)
    file.close()

def main():   
    ans = 'y'
    while ans == 'y':
        print(" 1) Add to file : ")
        print(" 2) View all records : ")
        print(" 3) Delete a record : ")
        print(" 4) Quit Program : ")
        selection = int(input("Enter the number of your selection : "))
        if selection == 1:
            add()
        elif selection == 2:
            view()
        elif selection ==3:
            delete()
        elif selection == 4:
            print("Quiting Program")
            ans = 'n'
        else:
            print("Wrong Choice, make selection again")


main()