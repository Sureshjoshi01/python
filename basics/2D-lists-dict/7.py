lt = {}
for i in range(0,2):
    name = input("Enter name of person : "  )
    age = int(input("Enter age : "))
    shoe = int(input("Enter shoe size : "))
    lt[name] = { "Age":age, "show":shoe}

for name in lt:
    print((name),lt[name]["Age"])