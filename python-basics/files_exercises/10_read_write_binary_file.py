# Write a program to read data from a binary file (“input.bin”) and write it to another binary file (“output.bin”).

input_file = "input.bin"
output_file = "output.bin"

try:
    with open(input_file,'rb') as input:
        content = input.read()

    with open(output_file,'wb') as output:
        output.write(content)

except Exception as e:
    print(f" {input_file} does not exists")
except Exception as e:
    print(f"{e} error occured")