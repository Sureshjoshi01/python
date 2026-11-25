# reverse a tuple 

# First Method
tuple1 = (10, 20, 30, 40, 50)
reverse_tuple = tuple1[::-1]
print(reverse_tuple)

# Second Method
tuple1 = (10, 20, 30, 40, 50 )
lst = list(tuple1)

start = 0
end = len(lst) - 1
while start < end:
    temp = lst[start]
    lst[start] = lst[end]
    lst[end] = temp
    start += 1
    end -= 1

print(tuple(lst))









