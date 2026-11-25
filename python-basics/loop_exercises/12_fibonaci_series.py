# Display Fibonacci series up to 10 terms


def fibonaci(n):
    first = 0
    second = 1
    print(first,end=" ")
    print(second,end=" ") 
    while n!=0:
        next_number = first + second
        first = second 
        second = next_number
        n = n - 1
        print(next_number,end=" ")

n = int(input("Enter number upto which fibonaci series is desired : "))
fibonaci(n)