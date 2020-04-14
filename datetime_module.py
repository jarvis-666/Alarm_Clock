import datetime
# naive objects are easier to work with which are not aware of time zones and daylight savings
# then there are aware objects

d = datetime.date(2020, 4, 23)
print(d)
# date is an object that represents date

tday = datetime.date.today()
print(tday)
print(tday.year)
# today() returns the current local date object

print(tday.weekday())
print(tday.isoweekday())
# Mon 0 Sun 6 for weekday
# Mon 1 Sun 7 for isoweekday

tdelta = datetime.timedelta(days=7)
print(tday - tdelta)
# adding or subtracting a timedelta from a date gives us date
# adding or subtracting two dates gives a timedelta
# timedelta is an object representing duration
print(*dir(tdelta), sep="\n")
bday = datetime.date(2021, 1, 27)
till_bday = bday - tday
print(till_bday.total_seconds())

t = datetime.time(1, 3, 30)
# also takes microseconds
print(t)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(*dir(dt))
# timedelta still works here

# Three types of constructors
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
# today() does not take time zone info
# now() is same as today() if tzinfo is None
# utcnow() is also not aware of time zone info
print(dt_today)
print(dt_now)
print(dt_utcnow)
