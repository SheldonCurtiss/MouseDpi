import ctypes

try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

import keyboard

def change_speed(speed=10):
    #   1 - slow
    #   10 - standard
    #   20 - fast
    print('changed')
    set_mouse_speed = 113  # 0x0071 for SPI_SETMOUSESPEED
    ctypes.windll.user32.SystemParametersInfoA(set_mouse_speed, 0, speed, 0)


def proper_close():
    change_speed(2)
    root.destroy()

root = tk.Tk()
root.protocol('WM_DELETE_WINDOW', proper_close)

tk.Button(root, text='~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~').pack(expand=True, fill='x')

# Sets to really slow so we can use desktop like normal
tk.Button(root, text='Desktop', command=lambda: change_speed(2)).pack(expand=True, fill='x')

# Sets to 6/11 so we can use in game
tk.Button(root, text='Gaming / Trackpad', command=change_speed).pack(expand=True, fill='x')

# Sets to REALLY slow for trackpad
# tk.Button(root, text='Trackpad', command=lambda: change_speed(20)).pack(expand=True, fill='x')

keyboard.add_hotkey('alt+1', lambda: change_speed(2))
keyboard.add_hotkey('alt+2', lambda: change_speed(10))

change_speed(2)
root.mainloop()
