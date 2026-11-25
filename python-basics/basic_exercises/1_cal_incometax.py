#Calculate income tax for the given income by adhering to the rules below
#Taxable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20


def income_tax(income):
    if income <= 10000:
        tax = 0
        return tax
    elif income > 10000:
        tax = ((10000 * 0)//100 + (10000 * 10)//100 + ((income - 20000)*20)//100)
        return tax

tax = income_tax(45000)
print(tax) 


