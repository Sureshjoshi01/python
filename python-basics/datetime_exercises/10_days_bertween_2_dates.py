# Write a code to calculate the days between two dates.

from datetime import datetime, timedelta, date

# 2020-02-25
date_1 = datetime(2020, 2, 25).date()
print(date_1)

# 2020-09-17
date_2 = datetime(2020, 9, 17).date()
print(date_2)

delta = date_2 - date_1
days_between_dates = delta.days

print(days_between_dates)