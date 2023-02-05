import datetime

birth_day=datetime.datetime(2020,11,22)
print(birth_day)

now=datetime.datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(now.date())
print(now.time())

now_date=now.strftime("%Y/%m/%d")
print(now_date)

now_time=now.strftime('%H시 %M분 %S초')
print(now_time)