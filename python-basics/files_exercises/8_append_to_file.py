# Modify the previous program to append the string “This is an appended line.” to the end of “output.txt”.

try:
    with open("output.txt","a") as f:
        f.write("\nThis is an appended line.")
except Exception as e:
    print(f"an error occured {e}")

