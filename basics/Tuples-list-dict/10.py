from sqlite3 import ProgrammingError


program = ["Star Wars","WWE","Contra","Tekken"]
for i in program:
    print(i)

name = input("Enter name of program : ")
pos = int(input("Enter position : "))
program.insert(pos,name)

print(program)