import tkinter as tk
from tkinter import ttk

def ChemicalEquation(self):
    # Top Labels
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.helloUserLab = ttk.Label(self.welcomeFrame, text="Chemical Equation Balancer", font=("TkDefaultFont",50,'bold'))
    self.helloUserLab.pack(pady=2)

def notUsable(self):
    # Top Labels
    self.notUsable = ttk.Frame(self.notebook)
    self.notUsable.pack(anchor="w")
    self.wipText = ttk.Label(self.notUsable, text="This is a Work in Progress", font=("TkDefaultFont", 30, 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = ttk.Label(self.notUsable, text="Check back soon!", font=("TkDefaultFont", 20), justify="center")
    self.wipTextA.pack(side="top", pady=2)
