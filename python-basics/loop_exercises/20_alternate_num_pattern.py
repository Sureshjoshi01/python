#Print the alternate numbers pattern

#Pattern:

#1  
##2 3  
#4 5 6  
#7 8 9 10  
#11 12 13 14 15

def alternate_number_pattern(rows):
    num = 1
    for i in range(1, rows + 1):
        if i % 2 != 0: 
            for x in range(num, num + i):
              print(x, end=' ')
            print() 
        else: 
            for y in range(num + i - 1, num - 1, -1):
              print(y, end=' ')
            print() 
        num += i

alternate_number_pattern(5)