# Calculate the date 4 months from the current date

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


given_date = datetime(2020, 2, 25).date()
print(given_date)

future_date_after_4_months = given_date + relativedelta(months=4)
print(future_date_after_4_months)