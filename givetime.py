import datetime

h, m = map(int, input("Set time for alarm: ").split())
alarm_set_time = datetime.time(h, m)

print(f"Alarm set for {alarm_set_time}")

date_today = datetime.date.today()

full_info = datetime.datetime.combine(date_today, alarm_set_time)

print(full_info)

status_ready = datetime.datetime.strptime(str(full_info), '%Y-%m-%d %H:%M:%S').strftime('%a %b %d %I:%M:%S %p %Y')
print(status_ready)