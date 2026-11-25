# Write a program to calculate the sum of this series up to n terms. 
# For example, if the number is 2 and the number of terms is 5, then the series will be 2+22+222+2222+22222=2469


def sum_series(n,t):
    sum = n
    current_term = n
    for i in range(0,t-1):
        current_term = n + (current_term * 10)
        sum = sum + current_term
    return sum

n = int(input("Enter Number : "))
t = int(input("Enter terms : "))
print(sum_series(n,t))
