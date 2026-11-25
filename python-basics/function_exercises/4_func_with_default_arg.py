#Write a program to create a function show_employee() with the following specifications:

#    It should accept the employee’s name and salary.
#    It should display both the name and salary.
#    If the salary is not provided in the function call, it should default to 9000.


def show_employee(name,sal=9000):
    print(name,sal)

show_employee("Rakesh",10000)
show_employee("Rajeev")
