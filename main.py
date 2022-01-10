from tkinter import *
from tkinter import ttk
from tkinter.font import families
import settings

# Configuration
settings.init()

# Home UI
rootWindow = Tk()
frame = ttk.Frame(rootWindow, padding=10)
frame.grid()
ttk.Label(frame, text="TooBox").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=rootWindow.destroy).grid(column=1, row=0)
rootWindow.mainloop()