# Print Current Date and Time

import datetime

current_date = datetime.datetime.now()
current_time = datetime.datetime.now().time()
current_day  = datetime.datetime.now().day
print("Current Date : ", current_date)
print("Current time : ", current_time)
print("Current day : ", current_day)

