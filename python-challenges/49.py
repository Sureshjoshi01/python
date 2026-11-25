# Question 49

# Write a program which can map() to make a list whose elements are square of 
# numbers between 1 and 20 (both included).


def even_num(n):
    if n % 2 == 0:
        return n

lst = []
for i in range(1,21):
    lst.append(i)
lst_even = map(even_num,lst)

result = [x for x in lst_even if x is not None]

print(result)