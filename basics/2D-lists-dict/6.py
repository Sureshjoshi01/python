lt = {}
for i in range(0,4):
    name = input("Enter name of person : "  )
    age = input("Enter age : ")
    shoe = input("Enter shoe size : ")
    lt[name] = { "Age ":age, "show":shoe}

ask = input("Enter a name : ")
print(lt[ask])