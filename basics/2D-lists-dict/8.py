lt = {}
for i in range(0,2):
    name = input("Enter name of person : "  )
    age = int(input("Enter age : "))
    shoe = int(input("Enter shoe size : "))
    lt[name] = { "Age":age, "show":shoe}

ask = input("Enter name you want to delete : ")
del lt[ask]

for name in lt: 
    print(lt[name])