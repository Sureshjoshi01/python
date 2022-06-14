countries = ("India","Russia","Japan","Ukraine","China")

print( countries )

c = int(input("Enter a number between 0 and 4 : "))
print(countries[c], "is at position ",c,"in tuple")

for i in range(len(countries)):
    if c == i:
        print(countries[i], "is at position ",c,"in tuple")