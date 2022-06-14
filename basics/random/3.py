import random 
num = random.choice(["h","t"])
str = input("Make a choice beteen head or tail(h/t) : "  )
if str.lower() == num:
    print("You Win")
else: 
    print("Bad Luck")
print("Computer choice was : ", num)

