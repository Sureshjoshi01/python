#Write a code to add a week (7 days) and 12 hours to a given date.

from datetime import datetime, timedelta

given_date = datetime(2020, 3, 22, 10, 0, 0)

future_date_after_adding_1_week = given_date + timedelta(weeks=1,hours=12)

print(future_date_after_adding_1_week)