from datetime import datetime

today = datetime.now()
a = str(today)[:10].replace("-", "")
b = today.strftime("%Y%m%d")

print(a)
print(b)
