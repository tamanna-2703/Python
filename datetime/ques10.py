from datetime import datetime

# 202-02-25
date_1 = datetime(2022, 2, 25).date()
# 2020-09-17
date_2 = datetime(2024, 9, 17).date()

delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")
