#Write all content of a file into a new file by skipping line number 5

f = open("test.txt","r")

l = f.readlines()
print(l)


for i in range(0,len(l)):
    if i == 4:
        continue
    f = open("new_file.txt","a")
    f.writelines(l[i])



