#Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. 
# Exit”. Based on the user’s input, perform the corresponding action


def interactive_menu(choice):
    if choice == 1:
        print("Hello")
    elif choice == 2:
        print("Calculate Square")
        n = int(input("Input number whose square is needed to be calculated :"))
        sq = n **2 
        print(f"Square of {n} : {sq}")
    else:
        print("Quitting Program")
        exit

print("\nMenu:")
print("1. Say Hello")
print("2. Calculate Square")
print("3. Exit")
choice = int(input("Enter your choice : "))
ans = True
while ans == True:
    
    if choice >= 3:
        ans = False
    else:
        interactive_menu(choice)
        choice = int(input("Do you want to enter more choices : "))
    

