def add():
    name = input("Enter Name to add : ")
    names.append(name)

def change():
    name = input("Enter Name to change : ")
    name2 = input("Enter Name which will replace : ")
    ind = names.index(name)
    names[ind] = name2

def delete():
    name = input("Enter Name to delete : ")
    ind = names.index(name)
    del names[ind]

def view():
    print("Names in List : ")
    for i in names:
        print(i)


def main():
    
    ans = 'y'
    while ans == 'y':
        print(" 1) Add a Name   ")
        print(" 2) Change a Name  ")
        print(" 3) Delete a Name   ")
        print(" 4) View all Names  ")
        print(" 5) Exit Program (y/n) : ")
        choice = int(input("Enter your choice  : "))
        if choice == 1:
            add()
        elif choice == 2:
            change()
        elif choice == 3:
            delete()
        elif choice == 4:
            view()
        elif choice == 5:
            print("Exiting Program, thanks bye")
            ans = 'n'
        else:    
            print("Wrong Choice , Please choose again : ")

names = []
main()