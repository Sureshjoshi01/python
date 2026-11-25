#The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.

def multiplication():
    for i in range(1,11):
        print(i,end=' ')
        j=2
        while j!=11:
            print(j*i,end=' ')
            j = j + 1
        print("\n")
multiplication()