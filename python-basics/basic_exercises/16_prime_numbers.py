#Print Alternate Prime Numbers till 20

def prime_numbers(num):
    is_prime = True
    if (num == 0 or num == 1):
        is_prime = False
    else:   
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break
    return is_prime
    
lst = []
for i in range(2,20):
    if (prime_numbers(i) == True):
        lst.append(i)
print(f'All prime numbers from 1 to {20}: {lst}')

print(f'Alternate prime numbers from 1 to {20}:')

for i in range(0, len(lst), 2): 
    print(lst[i],end=" ")
