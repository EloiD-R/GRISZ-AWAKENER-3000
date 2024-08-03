from datetime import datetime

# Get the current date and time
now = datetime.now()

# Extract the components
hour = now.hour
minute = now.minute
second = now.second
day_number_of_month = now.day
month_number = now.month
year = now.year
day_name = now.strftime("%A")  # Full weekday name
month_name = now.strftime("%B")  # Full month name

# Print in the desired formats
print(f"{hour}:{minute}:{second}")
print(f"{day_number_of_month}-{month_number}-{year}")
print(f"{day_name} {day_number_of_month} of {month_name} {year}")
