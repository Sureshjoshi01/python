from array import *
from pickle import FALSE, TRUE 
arr = array('i',[])
print("Enter 5 numbers between 10 and 20 : ")
ans = FALSE
while ans == FALSE:
    n = int(input())
    if n < 10 or n > 20: 
        print("Outside the range, Enter again : ")
       
    else:
        arr.append(n)
        if len(arr) >= 5:
            ans = TRUE
for i in arr: 
    print(i)
