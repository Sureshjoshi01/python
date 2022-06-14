countries = ("India","Russia","Japan","Ukraine","China")

print( countries )

c = input("Enter country from above 5 : ")
print(c, "is at position ",countries.index(c),"in list")

for i in range(len(countries)):
    if c == countries[i]:
        print(c, "is at position ",i,"in list")
