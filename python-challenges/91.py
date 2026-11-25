# Question 91

# By using list comprehension, 
# please write a program to print the list after removing 
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155]
x = []
for i in range(len(l)):
    if i%2!=0:
        x.append(l[i])

print(x)

x1 = [l[i] for i in range(len(l)) if i % 2 != 0]
print(x1)