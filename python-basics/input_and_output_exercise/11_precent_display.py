# Ask the user for a numerator and a denominator. 
# Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).

def percent(numerator,denominator):
    if denominator == 0:
        print("Denominator can't be zero")
        exit
    else:
        percent = (numerator/denominator) * 100
        print(f"The percentage is: {percent:.2f}%")


numerator = float(input("Enter numerator : "))
denominator = float(input("Enter Denominator : "))
percent(numerator,denominator)

