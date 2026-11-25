#Print a downward half-pyramid pattern of stars
#* * * * *  
#* * * *  
#* * *  
#* *  
#*

def downward_star_pattern():
    num = 5
    for i in range(0,5):
        print()
        for j in range(num,0,-1):
            print("*",end=' ')
        num = num - 1

downward_star_pattern()

