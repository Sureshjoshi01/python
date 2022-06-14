
f= {}
for i in range(0,4):
    print("Enter your ",i,"favourite ")
    food = input()
    f[i]= food
print(f)

n = int(input("Enter food you want to get rid of : "))
del f[n]
print(sorted(f.values()))