#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes
import random 

n1 = int(input("Enter number of elements for first list : "))
n2 = int(input("Enter number of elements for second list : "))

a = random.sample(range(100), n1)
b = random.sample(range(100), n2)




print(a)
print(b)
c = [ x for x in set(a) if x in b  ]

print(c)
