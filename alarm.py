from tkinter import *
import datetime

root = Tk()
root.title("Alarm Clock")

main_frame = LabelFrame(root, pady=0, padx=0)
title_label = Label(main_frame, font='bold', text="ALARM")
set_label = Label(main_frame, text="Time to set the alarm for: ")
enter_time = Entry(main_frame, width=50, borderwidth=5)
alarm_set_time = datetime.time()
set_alarm_button = Button(main_frame, text="Set Alarm")
clear_button = Button(main_frame, text="Clear")
alarm_set_label = Label(main_frame, text="Alarm Set")

alarm_frame = LabelFrame(root)
display_label = Label(alarm_frame, text="Time to Wake Up")
stop_button = Button(alarm_frame, text="Stop")

main_frame.grid(row=0, column=0)
title_label.grid(row=0, column=0, pady=10)
set_label.grid(row=1, column=0, pady=10)
enter_time.grid(row=1, column=1, pady=10)
set_alarm_button.grid(row=2, column=0, pady=10)
clear_button.grid(row=2, column=1, pady=10)
alarm_set_label.grid(row=3, column=0, columnspan=3, pady=10)

alarm_frame.grid(row=1, column=0, pady=50, sticky=W+E)
display_label.grid(row=0, column=0, padx=180)
stop_button.grid(row=1, column=0, pady=10)
root.mainloop()