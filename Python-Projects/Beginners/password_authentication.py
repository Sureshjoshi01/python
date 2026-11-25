# PASSWORD AUTHENTICATION 

database = {"suresh.joshi": "123456", "suresh.man": "654321"}
username = input("Enter your username : ")
password = input("Enter password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = input("Enter Your Password Again : ")
        break
print("Verified")