month = int(input("Please enter month: "))
year = int(input("Please enter year: "))
current_month = int(input("Please enter current month: "))
current_year = int(input("Please enter current year: "))

year += 3
if current_year < year:
  print("The car is still under warranty")
elif current_year > year:
  print("The car is no longer under warranty")
elif current_month < month:
  print("The car is still under warranty")
else:
  print("The car is no longer under warranty")