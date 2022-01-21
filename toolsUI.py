import tkinter as tk
from tkinter import ttk

def ChemicalEquation(self):
    # Top Labels
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = ttk.Label(self.welcomeFrame, text="Chemical Equation Balancer", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(pady=2)
    self.infoLabel = ttk.Label(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'HCl(aq) + Na(s) -> NaCl(aq) + H2(g)'", font=("TkDefaultFont", 15))
    self.infoLabel.pack(side="left", pady=2)
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(side="bottom", padx=25, pady=18, anchor="w")

def notUsable(self):
    # Top Labels
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", anchor="w")
    self.wipText = ttk.Label(self.welcomeFrame, text="This is a Work in Progress", font=("TkDefaultFont", 30, 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = ttk.Label(self.welcomeFrame, text="Check back soon!", font=("TkDefaultFont", 20), justify="center")
    self.wipTextA.pack(side="top", pady=2)
