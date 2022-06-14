print("Enter name of three friends : ")
name1 = input()
name2 = input()
name3 = input()

party = [name1,name2,name3]

res = input("do you want to add more name ? (y/n)")

while res == 'y':
    
    party.append(input("Enter friends name : "))
    res = input("do you want to add more name ? (Y/N)")

print(party)
print("Friends who are invited : ")

for i in party:
    print(i)


namex = input("Enter 1 name from above list : ")

for i in range(len(party)):
    if namex == party[i]:
        print("position of namex : ", i )

print("Do you want ",  namex ,"to come to party ? (yes/no) :")
ques = input()
if ques == 'no':
    party.remove(namex)

print("Full lits of invitees : ", party)



      

