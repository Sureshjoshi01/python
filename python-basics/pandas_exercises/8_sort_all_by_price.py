# Exercise 8: Sort all cars by Price column

import pandas as pd

df = pd.read_csv("Automobile_data.csv")

print((df.sort_values(by="price")).head(5))

