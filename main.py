import os
import tkinter as tk
from tkinter import messagebox
import time

# shutdown -s -t XXXX


# GUI

window = tk.Tk()
window.title('Delayed shutdown and time sync utility')

window.rowconfigure([0, 1, 2, 3, 4], minsize = 100, weight = 1)
window.columnconfigure([0, 1, 2], minsize = 50, weight = 1)
window.geometry("500x260")

frame = tk.Frame(
    master = window,
    relief = tk.FLAT,
    borderwidth = 3,
    width = 500,
    height = 50
    )
frame.rowconfigure(0, minsize = 100, weight = 1)
frame.columnconfigure(0, minsize = 50, weight = 1)
frame.pack()

def shutdown():
    delay = txt_field.get()
    secs = int(delay) * 60
    cmd = 'shutdown -s -t ' + str(secs)
    messagebox.showinfo("Conunting", ('Shutdown commences in ' + str(delay) + ' minutes.' + "\nAfter you press OK"))
    os.system(cmd)

CMD_LIST = [
            ['stopping w32time' , 'net stop w32time'],
            ['unregistering w32time' , 'w32tm /unregister'],
            ['registering it back' , 'w32tm /register'],
            ['starting w32timeservice' , 'net start w32time'],
            ['resyncing' , 'w32tm /resync']
        ]

WIFI_LIST = ['netsh winsock reset',
             'netsh int ip reset',
             'netsh advfirewall reset',
             'ipconfig / flushdns',
             'ipconfig / release',
             'ipconfig / renew'
             ]


def clear():
    txt_field.delete(0, 'end')
    messagebox.showinfo('Done', 'cleared!')

def cancel():
    os.system('shutdown /a')
    messagebox.showinfo('Success', 'Shutdown cancelled')

lbl_sync = tk.Label(
    master = frame,
    text = 'Time sync is not initiated'
)
lbl_sync.grid(row = 3, column=1, sticky='nsew')

lbl_wifi_reboot = tk.Label(
    master = frame,
    text = 'Wifi sync is not initiated'
)
lbl_wifi_reboot.grid(row = 3, column=0, sticky='nsew')

def resync_time():
    for entry in CMD_LIST:
        lbl_sync.configure(text = entry[0])
        os.system(entry[1])
    lbl_sync.text = 'Should be done!'

def wifi_reboot():
    for entry in WIFI_LIST:
        lbl_wifi_reboot.configure(text = entry)
        os.system(entry)
    lbl_wifi_reboot.text = 'Should be done!'

lbl_header = tk.Label(
    master = frame,
    text = 'Please enter desired delay before shutdown in minutes'
    )
lbl_header.grid(row = 0, column = 1, sticky = 'nsew')

txt_field = tk.Entry(
    master = frame,
    width = 4
    )
txt_field.grid(row = 1, column = 1, sticky = 'nsew')


btn_subm = tk.Button(
    master = frame,
    text = 'Initiate',
    command = shutdown
)
btn_subm.grid(row = 1, column = 2, sticky = 'nsew')

btn_sync_time = tk.Button(
    master = frame,
    text = 'Initiate time sync',
    command = resync_time
    )
btn_sync_time.grid(row = 4, column = 1, sticky = 's')

btn_wifi_reboot = tk.Button(
    master = frame,
    text = 'Reboot wifi',
    command = wifi_reboot
    )
btn_wifi_reboot.grid(row = 4, column = 0, sticky = 'nsew')

btn_clear = tk.Button(
    master = frame,
    text = 'Clear field',
    command = clear
)
btn_clear.grid(row = 1, column = 0, sticky = 'w')

btn_cancel = tk.Button(
    master = frame,
    text = 'Cancel shutdown',
    command = cancel
    )
btn_cancel.grid(row = 2, column = 1, sticky = 's')


window.mainloop()
