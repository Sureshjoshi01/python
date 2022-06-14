from array import * 
import random 

arr1 = array('i',[])
arr2 = array('i',[])

print("Enter 3 numbers :" )
for i in range(0,3):
    n = int(input())
    arr1.append(n)


for i in range(0,5):
    n = random.randint(1,100)
    arr2.append(n)
print("\n")
arr1.extend(arr2)

arr1 = sorted(arr1)

print("Final array : ")
for i in arr1: 
    print(i)