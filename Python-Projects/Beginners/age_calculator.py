# Age Calculator 
from datetime import datetime, date

def age_calulator(birth_day,birth_month,birth_year):
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    if current_day < birth_day:
        current_month = current_month - 1
        current_day  = current_day + 30

   
    if current_month < birth_month:
        current_year  = current_year - 1
        current_month = current_month + 12

    no_of_days  = current_day   - birth_day
    no_of_month = current_month - birth_month
    no_of_year  = current_year  - birth_year
    
    
    return no_of_year, no_of_month, no_of_days
 

birth_day   = int(input("Enter your Day of Birth : "))
birth_month = int(input("Enter your Month of Birth : "))
birth_year  = int(input("Enter your Year of Birth : "))

today = date.today()
y,m,d = age_calulator(birth_day,birth_month,birth_year)
print("Your age af of ",today," is ", y,"years",m,"months",d,"days")