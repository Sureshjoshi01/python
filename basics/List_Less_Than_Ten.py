# write a program that prints out all the elements of the list that are less than 5.

mylist = []
lessthen5 = []
lessthenn = []
for i in range(1,12):
    num = int(input(f'Enter {i} element of list : '))
    mylist.append(num)

for i in mylist:
    if i < 5:
        print(i)

for i in mylist:
    if i < 5:
        lessthen5.append(i)
print(lessthen5)

n = int(input("Enter a number : "))
for i in mylist:
    if i < n:
        lessthenn.append(i)
print(lessthenn)
        