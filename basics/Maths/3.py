
import math
n = int(input("Enter number: "))
if n < 500:
    print("Enter number above 500")
    exit
else:
    sq = math.sqrt(n)
    print(sq)
    print(round(sq,2))
