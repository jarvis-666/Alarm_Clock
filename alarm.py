from tkinter import *
from tkinter import messagebox
import time
import datetime
import winsound

alarm_set_time = None
status_label = None

def update_clock():
    current_time = str(datetime.datetime.now().time())
    if current_time >= str(alarm_set_time):
        playAlarm()
        return
    else:
        root.after(1000, func=update_clock)


def playAlarm():
    winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav",
                       flags=winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    response = messagebox.showinfo(title="Wake Up!", message="Hey! It's time to wake up...")
    if response == 'ok':
        global status_label
        status_label.destroy()
        winsound.PlaySound(sound="C:\\Users\\Vin\\Downloads\\Alarm.wav", flags=winsound.SND_PURGE)
        alarm_state = 'OFF'
        top_label.config(text=f"ALARM {alarm_state}")
        status_label = Label(main_frame, text="Alarm not set", bd=1, relief=SUNKEN)
        status_label.grid(row=3, column=2)
        alarm_set_time = None


def set_alarm():
    global alarm_set_time
    global status_label
    alarm_set_time = time_entry.get()
    alarm_set_time = alarm_set_time.split(' ')
    alarm_set_time = datetime.time(int(alarm_set_time[0]), int(alarm_set_time[1]))
    alarm_state = "ON"
    top_label.config(text=f"ALARM {alarm_state}")
    date_today = datetime.date.today()
    full_info = datetime.datetime.combine(date_today, alarm_set_time)
    status_ready = datetime.datetime.strptime(str(full_info), '%Y-%m-%d %H:%M:%S').strftime('%a %b %d %I:%M:%S %p %Y')
    status_label = Label(main_frame, text=f"Alarm set for {status_ready}", bd=1, relief=SUNKEN)
    status_label.grid(row=3, column=2)
    update_clock()


def clear_alarm():
    time_entry.delete(0, END)

if __name__ == '__main__':
    root = Tk()
    root.title("Alarm Clock")

    main_frame = LabelFrame(root)
    alarm_state = 'OFF'
    top_label = Label(main_frame, text=f"ALARM {alarm_state}")
    set_alarm_label = Label(main_frame, text="Time to set alarm for:")
    time_entry = Entry(main_frame)
    set_alarm_button = Button(main_frame, text="Set Alarm", command=set_alarm)
    clear_alarm_button = Button(main_frame, text="Clear", command=clear_alarm)
    status_label = Label(main_frame, text="Alarm not set", bd=1, relief=SUNKEN)

    main_frame.pack()
    top_label.grid(row=0, column=2, padx=10, pady=10)
    set_alarm_label.grid(row=1, column=0, padx=10)
    time_entry.grid(row=1, column=3)
    set_alarm_button.grid(row=2, column=0, pady=10)
    clear_alarm_button.grid(row=2, column=3, padx=10, pady=10)
    status_label.grid(row=3, column=2)

    root.update_idletasks()
    root.mainloop()
