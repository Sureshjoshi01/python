list_a = [1,2,4,3,6]


def test(list_a):
    n = len(list_a)
    for i in range(n):
        for j in range(i+1,n):
            if list_a[i] == list_a[j]:
                return False
        
    return True

x = test(list_a)
print(x)
    
