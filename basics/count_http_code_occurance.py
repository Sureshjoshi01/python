
#Write a Python script that reads a log file and counts the number of occurrences of each status code (e.g., 200, 404, etc.).

status_codes = [100,101,102,200,201,202,203,204,205,206,207,208,226,300, 301, 302, 303, 304, 305, 306, 307, 308,401,402,403,404,405,406,407,408,409,410,412,413,414,415,416,417,418,500,501,502,503,504,505,51]
def read_file():
    lst = []
    file = open("nginx.log","r")
    for line in file:
        line1 = line.split(' ')
        line1.pop()
        status_code_lst = line1.pop()
        lst.append(status_code_lst)
    print(lst)
    for i in status_codes:
        if str(i) in lst:
            print(f'Number of occurence of HTTP status code {i} : ', lst.count(str(i)))

read_file()