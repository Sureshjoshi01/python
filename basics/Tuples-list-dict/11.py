nums =[]

count = 0
while count < 3:
    num = int(input("Enter number : "))
    nums.append(num)
    print(nums)
    count = count + 1 
lastnum = input("Do you want the last number saved (y/n) : ")
if lastnum == "n":
    nums.remove(num)
print(nums)   
