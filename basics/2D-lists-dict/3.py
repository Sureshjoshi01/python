list_d = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]

r =int(input("Enter row number : "))
print(list_d[r])
ans = 'Y' 

c = int(input("which column in selected row : "))
print(list_d[r][c])

q = input("do you want to change the column value (y/n): ")
if ans.upper() == 'Y':
    d = int(input("Enter new column value : "))
    list_d[r][c] = d 
print(list_d[r]) 



