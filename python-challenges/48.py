# Question 48

# Write a program which can filter() to make a list 
# whose elements are even number between 1 and 20 (both included).


def even_num(n):
    return n % 2 == 0

lst = []
for i in range(1,21):
    lst.append(i)
lst_even = filter(even_num,lst)

print(list(lst_even))