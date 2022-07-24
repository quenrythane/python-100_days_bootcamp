from datetime import datetime, timedelta

def week_interval(date: tuple):
    today = datetime(date[0], date[1], date[2])
    start_week = datetime(today.year, today.month, today.day - (today.isoweekday() - 1))
    end_week = start_week + timedelta(days=6)
    return start_week.strftime("%Y%m%d"), end_week.strftime("%Y%m%d")


date = (2022, 7, 24)
print(week_interval(date))
print(datetime(2022, 6, 30), type(datetime(2022, 6, 30)))


# 18-24
# 24 - (iso - 1) // 24 + ( 7 - iso)

# 18 //