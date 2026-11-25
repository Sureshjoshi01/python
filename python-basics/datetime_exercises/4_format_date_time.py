# Write a code to print date in the following format.

from datetime import datetime

given_date = datetime(2020, 2, 25)
formatted_date = given_date.strftime("%A %d %B %Y")

print(formatted_date)