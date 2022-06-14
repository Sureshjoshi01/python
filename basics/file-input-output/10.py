import csv

sy = int(input("Enter starting year : "))
ey = int(input("Enter ending year : "))
file = list(csv.reader(open("Books.csv")))
tmp = []

for row in file: 
    tmp.append(row)

x = 0 
for row in tmp: 
    if int(tmp[x][2]) >= sy and int(tmp[x][2]) <= ey: 
        print(tmp[x])
    x = x+1
