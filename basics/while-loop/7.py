n = 10

while n > 0: 
    print("There are ", n , "green bottles hanging on the wall")
    print( n, "green bottles hanging on the wall")
    print(" and if 1 green bottle should accidentally fall")
    n = n-1 
    ans = int(input("How many green bottle will be hanging on the wall ? "))
    if ans == n:   
        print("There will be ", n , "green bottles on the wall" )
    else:
        while ans != n:
            ans = int(input("No, try again : "))
    
    print("There are no more green bottles hanging on the wall ")




