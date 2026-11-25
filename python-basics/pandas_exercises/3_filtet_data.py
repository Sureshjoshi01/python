# Print most expensive car’s company name and price.

import pandas as pd 

df = pd.read_csv("Automobile_data.csv")

df = df.loc[df['price'] == df['price'].max(), ['company', 'price']]
print(df)