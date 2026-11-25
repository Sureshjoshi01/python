def is_leap_year(year):
  """
  Returns:
    True if the year is a leap year, False otherwise.
  """
  print("Year", year)
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# check
print(is_leap_year(2020)) # True
print(is_leap_year(2025)) # False