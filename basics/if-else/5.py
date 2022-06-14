rain = input("Is it raining ? ")
lo1 = str.lower(rain)

if lo1 == "yes":
    wind = input("Is it Windy ? ")
    lo2 = str.lower(wind)
    if lo2 == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy Your Day")
