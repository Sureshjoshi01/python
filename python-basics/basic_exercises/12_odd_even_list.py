#Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

n1 = int(input("How many numbers you want in first list : "))
n2 = int(input("How many numbers you want in second list : "))

lst1 = []
lst2 = []
lst3 = []

print("Enter numbers to be added to first list : ")
for i in range(n1):
    num = int(input())
    lst1.append(num)
print(lst1)

print("Enter numbers to be added to second list : ")
for i in range(n2):
    num = int(input())
    lst2.append(num)
print(lst2)


for i in lst1:
    if (i % 2) != 0:
        lst3.append(i)
for i in lst2:
    if (i % 2) == 0:
     lst3.append(i)

print("list containing odd numbers from the first list and even numbers from the second list")
print(lst3)