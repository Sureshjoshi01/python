# Create a function with keyword arguments

def print_info(**kwargs):
    if kwargs:  # Check if any keyword arguments were passed
        print("\n--- Information ---")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("\nNo information provided.")




print_info(animal_type='cat', pet_name='Whiskers')
print_info(pet_name='Buddy', animal_type='goldfish')
    