from array import * 
arr = array('i',[34,56,76,34,67])
for i in arr:
    print(i)
print("Enter number from the above list : ")
no = int(input())


print(no," appears ",arr.count(no),"times in array")