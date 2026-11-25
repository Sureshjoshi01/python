#Print Reverse Number Pattern


def downward_number_pattern():
    num = 5
    for i in range(0,5):
        print()
        for j in range(num,0,-1):
            print(i+1,end=' ')
        num = num - 1

downward_number_pattern()