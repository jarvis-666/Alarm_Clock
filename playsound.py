import winsound
import time

winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav", flags=winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
time.sleep(10)
winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav", flags=winsound.SND_PURGE)

