import tkinter as tk
from tkinter import ttk

class SettingsSlider(ttk.Label):
    def __init__(self, master=None, **kwargs):
        ttk.Scale.__init__(self, master, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))