# Question 96

# Please write a program which count and print the numbers of each character in a 
# string input by console.

# Example: If the following string is given as input to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2 c,2 b,2 e,1 d,1 g,1 f,1



s = input()
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
for ch, cnt in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print(f"{ch},{cnt}", end=" ")