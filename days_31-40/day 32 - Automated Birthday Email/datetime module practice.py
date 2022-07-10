import datetime as dt


now = dt.datetime.now()  # datatime object
print(now, type(now))
print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
print("weekday:", now.weekday(), "\n")
# weekday() returns 0 for Monday, 1 for Tuesday, etc.

print(type(now.year), type(now.month), type(now.day ))
print(now.strftime("%Y-%m-%d %H:%M:%S"), "\n")

date_of_birth = dt.datetime(year=1990, month=1, day=20)
print(date_of_birth)
