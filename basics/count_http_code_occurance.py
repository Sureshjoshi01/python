
#Write a Python script that reads a log file and counts the number of occurrences of each status code (e.g., 200, 404, etc.).

def read_file():
    file = open("nginx.log","r")
    for line in file:
        line1 = line.rstrip('/"')
        print(line1)

read_file()