# example https://public.karat.io/content/referrals_4.txt
# output should be ['public.karat.io','karat.io']

import requests
str = []
file = open("referrals.txt", "a")

url="https://public.karat.io/content/referrals_4.txt"
response = requests.get(url)
file.write(response.text)
file.close()

with open("referrals.txt","r") as file:
    for line in file:
        line1 = line.replace('https://','')
        line1 = line1.replace('http://','')
        line1 = line1.replace('\n','')
        line1 = line1.split('/')
        str.append(line1[0])

for i in str:
    i1 = i.split('.')
    i1 = i1[-2] + "." + i1[-1]
    lst = [i,i1]
    print(lst)


