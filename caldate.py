import calendar
from datetime import datetime as dt
print(calendar.calendar(2023))
now = dt.now()
print(now)
print(type(now))

print(now.strftime('%y-%m-%d'))
print("요일 : {} ".format(now.weekday())) #월(0), 화(1)

print(now.strftime('%H:%M:%S:'),now.microsecond)
#print("마이크로초 : {} ".format(now.microsecond))

