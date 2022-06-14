import csv 

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x  = 0 
for i in tmp:
    display = "Row: " + str(x) + "- " + str(i)
    print(display)
    x = x+1 

rdel = int(input("Which row you want ot delete : "))

del tmp[rdel]

x  = 0 
for i in tmp:
    display = "Row: " + str(x) + "- " + str(i)
    print(display)
    x = x+1 

rchg = int(input("Which row you want to change : "))
x = 0 
for i in tmp[rchg]:
    display = x,tmp[rchg][x]
    print(display)
    x= x+1
part =  int(input("Which part yu want to change : "))
newdata =  input("Enter new data : ")
tmp[rchg][part] = newdata
print(tmp[rchg])

file = open("Books.csv","w")
x = 0
for row in tmp:
    newrecord = tmp[x][0] + " , " + tmp[x][1] + " , " + tmp[x][2] + "\n"
    file.write(newrecord)
    x = x+1 
file.close()


