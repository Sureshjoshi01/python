subject = ["maths","science","english","history","geography"]

print(subject)
sub = input("Enter Suject from above you done line: ")
for i in range(len(subject)):
    if sub == subject[i]:
        c = i

del subject[c]

        

print(subject)
