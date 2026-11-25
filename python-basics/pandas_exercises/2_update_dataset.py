# Replace all column values which contain ?, n.a, or NaN.

import pandas as pd
import numpy as np

df = pd.read_csv("Automobile_data.csv")

df = df.replace(['?', 'n.a', 'N.A', 'NaN'], np.nan, inplace=True)

print(df)