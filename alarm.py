from tkinter import *
from tkinter import messagebox
import time

def button_pop():
    response = messagebox.showinfo(title="Wake Up!", message="Hey! It's time to wake up...")
    if response == 'ok':
       Label(root, text="Alarm OFF").pack()
    # Label(root, text=response).pack()

root = Tk()
root.title("Alarm Clock")

main_frame = LabelFrame(root)
alarm_state = 'OFF'
top_label = Label(main_frame, text=f"ALARM {alarm_state}")
set_alarm_label = Label(main_frame, text="Time to set alarm for:")
time_entry = Entry(main_frame)
set_alarm_button = Button(main_frame, text="Set Alarm")
time_entered = time.asctime(time.localtime())                               ## temporary
clear_alarm_button = Button(main_frame, text="Clear")
status_label = Label(main_frame, text=f"Alarm set for {time_entered}", bd=1, relief=SUNKEN)
demo_button = Button(root, text="demo", command = button_pop)               ## This is temporary

main_frame.pack()
top_label.grid(row=0, column=2, padx=10, pady=10)
set_alarm_label.grid(row=1, column=0, padx=10)
time_entry.grid(row=1, column=3)
set_alarm_button.grid(row=2, column=0, pady=10)
clear_alarm_button.grid(row=2, column=3, padx=10, pady=10)
status_label.grid(row=3, column=2)
demo_button.pack()

root.mainloop()
