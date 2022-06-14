from array import * 
import random
arr = array('i',[])
for i in range(0,5):
    n = random.randint(1,100)
    arr.append(n) 
for i in arr:
    print(i)