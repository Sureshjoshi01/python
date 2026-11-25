# Write a Python program to create a new file named “output.txt” and write the string “Hello, PYnative!” into it.
try:
    with open("output.txt","w") as f:
        f.write("Hello, PYnative!")
except Exception as e:
    print(f"An error occured {e}")
