
invite_list = []
print("Enter name of three friends you like to invite : ")
for i in range(0,3): 
    invite_list.append(input())
print(invite_list)


a = True
while a == True:
    ans = input("Do you want to enter more name (yes/no) : ")
    if ans.upper() == 'YES':
        invite_list.append(input("Enter friend name "))
    elif ans.upper() == 'NO':
        print("Number of friends invited by you : ", len(invite_list)) 
        a = False

    