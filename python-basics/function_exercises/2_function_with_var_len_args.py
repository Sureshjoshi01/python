# Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.

def func1(*args):
    for arg in args:
        print(arg)

func1(10,20,30)
func1(10,20,30,40)
