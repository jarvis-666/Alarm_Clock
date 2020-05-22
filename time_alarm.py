import datetime
import time
import winsound

h, m = map(int, input("Set time for alarm: ").split())
alarm_set_time = datetime.time(h, m)

print(f"Alarm set for {alarm_set_time}")

stop = False
while not stop:
    current_time = str(datetime.datetime.now().time())
    if current_time >= str(alarm_set_time):
        stop = True

winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav", flags=winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
time.sleep(10)
winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav", flags=winsound.SND_PURGE)