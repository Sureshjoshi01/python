# Exercise 9: Concatenate two data frames using the following conditions

import pandas as pd 

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

df1 = pd.DataFrame.from_dict(GermanCars)
print(df1)

df2 = pd.DataFrame.from_dict(japaneseCars)
print(df1)


carsDf = pd.concat([df1, df2], keys=["Germany", "Japan"])
carsDf