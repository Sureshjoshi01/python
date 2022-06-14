from array import *
arr = array('i',[])
n2  = array('i',[])
print("Enter 5 numbers : ")
for i in range(0,5):
    n = int(input())
    arr.append(n)
arr = sorted(arr)
print(arr)

n = int(input("Select one of the number from above : "))
arr.remove(n)
print(arr)
n2.append(n)
print(n2)

for i in range(0,2):
    n = int(input())
    n2.append(n)

print(n2)
