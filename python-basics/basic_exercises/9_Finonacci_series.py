#Generate Fibonacci series up to 15 terms

def fibonacci(num):
    first_num = 0
    second_num = 1
    print(first_num,end=' ')
    for i in range(1,num):
        next_num = first_num + second_num
        second_num = first_num
        first_num = next_num 
        print(next_num,end=' ')

fibonacci(15)




        
