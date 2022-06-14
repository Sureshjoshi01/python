from array import *
from pickle import TRUE
from tkinter import FALSE 
arr = array('i',[12,32,54,67,89])
print("Numbers in array : ")

for i in arr: 
    print(i)




ans = FALSE
n = int(input("Select number from list : "))
while ans == FALSE: 
    
    for i in range(len(arr)): 
        if n == arr[i]:
            print("Position of ", n," is ", i)
            ans = TRUE
        else:
            int(input("Try again, select relevent item : "))
            

    
