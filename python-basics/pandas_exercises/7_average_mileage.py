#Exercise 7: Find the average mileage of each car making company

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
car_Manufacturers = df.groupby("company")
mileageDf = car_Manufacturers["average-mileage"].mean()
print(mileageDf)