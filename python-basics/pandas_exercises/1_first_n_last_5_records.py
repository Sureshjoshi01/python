# Exercise 1: From the Automobile_data.csv dataset print the first and last five rows

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
first_five = df.head(5)
last_five = df.tail(5)
print(first_five)
print()
print(last_five)


