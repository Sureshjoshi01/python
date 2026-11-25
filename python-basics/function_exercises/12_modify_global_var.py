# Define a global variable global_var = 10. Write a function that modifies a global variable value.

global_var = 10

def mod_global_var():
    global global_var
    global_var = global_var + 15
    return global_var

print(global_var)
print(mod_global_var())


