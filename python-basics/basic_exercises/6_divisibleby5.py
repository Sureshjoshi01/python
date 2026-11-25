#Write a Python code to display numbers from a list divisible by 5
import sys

def divisible_by_5(lst):
    for i in lst:
        if int(i) % 5 == 0:
            print(i)
lst = sys.argv[1:]

divisible_by_5(lst)
