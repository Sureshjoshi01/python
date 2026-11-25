# Question 25

# Level 1

# Question: Define a class, which have a class parameter and have a same 
# instance parameter.

# Hints: Define a instance parameter, need add it in init method 
# You can init a object with construct parameter or set the value later

class employee:
    company_name = "Siemens"    # class parameter
    raise_by_amount = 1.05
    def __init__(self,name,salary):
        self.name = name              # instance parameter
        self.salary = salary 

emp1 = employee("Suresh","40000")
emp2 = employee("Jack","3000")

print(emp1.company_name)
print(emp1.name)
print(emp1.salary)
print(emp2.company_name)
print(emp2.name)
print(emp2.salary)