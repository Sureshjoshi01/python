# Write a program to create a simple text editor. This program allows users to open
# an existing text file or create a new one, edit the content, and then save the
# changes by typing the SAVE command.
# Optional Enhancements
# • Allow users to choose whether they want to overwrite the existing file content
# or append new text to the end of the file.


from pathlib import Path

def write_to_file(filename,lines,ans):
    if ans == 'overwrite':
        mode = "w"
    else:
        mode = "a"
    with open(filename,mode) as file:
        for i in lines:
            file.write(f"{i}\n")
        

def main():
    lines = []
    print("Enter the filename to open or create: ",end="")
    while True:
            filename = input()
            file_path = Path(filename)
            if len(filename) == 0:
                print("Enter valid filename")
                continue
            elif not file_path.is_file():
                print(f"{filename} not found. Creating a new file.")
                ans = 'append'
            elif file_path.is_file():
                print(f"{filename} already exists")
                with open(filename, "r") as file:
                    print(file.read())
                print("Do you want to overwrite the existing file content or append new text to the end of the file ?")
                while True:
                    ans = input().lower()
                    if ans in ['overwrite','append']:
                        break
                    else:
                        print("You need to enter overwrite or append !")
            
            break  

    print("Enter your test (type 'SAVE' on a new line to save and exit):")
    while True:
        line = input().strip()
        if line == "SAVE":
            break
        lines.append(line)
    
    write_to_file(filename,lines,ans)
    print(f"File {filename} saved")

main()
