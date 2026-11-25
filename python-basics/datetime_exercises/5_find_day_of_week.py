# Write a code to find the day of the week of a given date.


from datetime import datetime 

given_date = datetime(2020, 7, 26)

day_of_week = given_date.today().weekday()
print(given_date.strftime('%A'))
print(day_of_week)