# Character Input
import string
from datetime import date

name = input("Enter you name : ")
age  = int(input("Enter your age : "))
num  =  int(input("Enter a number : "))

current_year = date.today().year
age_100_old = (100 - age) + current_year

for i in range(num):
    print(f'{name} will be 100 years old in {age_100_old}')