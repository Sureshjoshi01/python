mylist = [5,2,6,8,3,9]
def swapin(listin,pos1,pos2):
    temp = pos1
    listin[pos1] = listin[pos2]
    listin[pos2] = temp

p1 = int(input("Enter position 1 : "))
p2 = int(input("Enter position 2:"))
print("Enter positions",p1,p2)
swapin(mylist,p1,p2)
print(mylist)


