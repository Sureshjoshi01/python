# write a program that returns a list that contains only the elements that are common between the lists


def lista():
    a = []
    flag = True
    n = int(input("Enter Elements of first list :   \n"))
    a.append(n)
    while flag == True:
        c = input("Do you want to enter more elemets(y/n) : ")
        if c.lower() == 'n':
            flag = False
        elif c.lower() == 'y':
            n = int(input())
            a.append(n)
        else:
            print("You need to enter y or n ")
    return a

def listb():
    b= []
    flag = True
    n = int(input("Enter Elements of second list :   \n"))
    b.append(n)
    while flag == True:
        c = input("Do you want to enter more elemets(y/n) : ")
        if c.lower() == 'n':
            flag = False
        elif c.lower() == 'y':
            n = int(input())
            b.append(n)
        else:
            print("You need to enter y or n ")
    return b

def list_overlap(a,b):
    c = []
    for i in a:
        for j in b:
            if i == j:
                c.append(i)
    return c

def main():
    a = []
    b = []
    c = []
    a = lista()
    print(a)
    b = listb()
    print(b)
    c = list_overlap(a,b)
    print(c)
    listc = set(c)  # convert list to set for non duplicate elements
    print(listc)

main()


