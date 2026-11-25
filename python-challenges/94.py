# Question 94

# With a given list [12,24,35,24,88,120,155,88,120,155], write a program 
# to print this list after removing all duplicate values with original order 
# reserved.

l = [12,24,35,24,88,120,155,88,120,155]
x = []
final_list = []
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            x.append(l[i])

for i in l:
    if i not in x:
        final_list.append(i)
print(x)
print(final_list)