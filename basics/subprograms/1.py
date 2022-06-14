def input_number():
    num = int(input("Enter a number: "))
    return num

def count_num(num):
    for i in range(1,num):
        print(i)


x = input_number()
count_num(x)
    