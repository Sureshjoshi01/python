#Write a code to subtract a week (7 days) from a given date.

from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
date_week_ago = given_date - timedelta(weeks=1)

print(date_week_ago.date())

