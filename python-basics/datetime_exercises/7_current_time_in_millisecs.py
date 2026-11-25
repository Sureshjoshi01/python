# Print Current Time in Milliseconds
# 1st way 
from datetime import datetime

now = datetime.now()
total_milliseconds = (
    now.hour * 3600 * 1000 +
    now.minute * 60 * 1000 +
    now.second * 1000 +
    now.microsecond // 1000
)
print("Current time since midnight in milliseconds:", total_milliseconds)

# 2nd way 

import time

milliseconds = int(round(time.time() * 1000))
print(milliseconds)