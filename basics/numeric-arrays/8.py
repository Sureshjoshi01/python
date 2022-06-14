from array import * 
import math
arr = array('f',[11.22,22.11,33.44,55.44,66.77])
ask = True
while ask == True: 
    num = int(input("Enter a number between 2 and 5 : "))
    if num <2 and num>5:
        print("Incorrect value, try again")
    else: 
        ask = False
for i in range(0,5):
    ans = arr[i]/2
    print(round(ans,2))