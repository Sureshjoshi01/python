# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

def sum_and_avg_of_digits_in_str(str1):
    sum = 0
    count = 0
    for i in str1:
        if i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            count = count + 1
            sum = sum + int(i)
    avg = sum/count
    return sum,avg


str1 = "PYnative29@#8496"
sum,avg = sum_and_avg_of_digits_in_str(str1)

print("Sum is : ",sum, "Average is : ", avg)

str1 = "jack123wer456rtu789"
sum,avg = sum_and_avg_of_digits_in_str(str1)

print("Sum is : ",sum, "Average is : ", avg)