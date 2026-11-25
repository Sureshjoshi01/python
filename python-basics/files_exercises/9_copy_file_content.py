# Write a program that takes two filenames as input (source and destination) and copies the content of the source file to the destination file.

source_file = "Tasks_Today.txt"
destination_file = "output.txt"

try:
    with open(source_file,'r') as source:
        contents = source.read

    with open(destination_file,'w') as destination:
        destination.write(contents)

except Exception as e:
    print(f" {source_file} file does not exists")



