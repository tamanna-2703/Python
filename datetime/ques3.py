from datetime import datetime, timedelta

given_date = datetime(2024, 8, 1)
print("Given date")
print(given_date)

days_to_subtract = 7
res_date = given_date - timedelta(days=days_to_subtract)
print("New Date")
print(res_date)
