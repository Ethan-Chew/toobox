import tkinter as tk
from tkinter import ttk
import re
from tools.IonicEqn import ionicEqn

from tools.balancingChemEqn import balanceChemEqn
from components.wrappedLabel import WrappingLabel
from tools.saltSolubilities import saltSolubilities

def ChemicalEquation(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = balanceChemEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)
    
    # User Interface
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Chemical Equation Balancer", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=("TkDefaultFont", 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=("TkDefaultFont", 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=("TkDefaultFont", 12))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)
    
    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def notUsable(self):
    # Top Labels
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", anchor="w")
    self.wipText = WrappingLabel(self.welcomeFrame, text="This is a Work in Progress", font=("TkDefaultFont", 30, 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = WrappingLabel(self.welcomeFrame, text="Check back soon!", font=("TkDefaultFont", 20), justify="center")
    self.wipTextA.pack(side="top", pady=2)

def Rectangle(self):
    def getInputs(self):
        answer = "Ensure that both values, i.e. Breadth/Width and Length, are numbers"
        length = str(self.lengthEntry.get())
        breadth = str(self.breadthEntry.get())
        if re.match("^\d+?\.{0,1}\d+?$", length) and re.match("^\d+?\.{0,1}\d+?$", breadth):
            print("came ")
            answer = float(length)*float(breadth)
        setFinalResult(self, answer)
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Rectangle/Square Area Calculator", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.breadthTxt = WrappingLabel(self.mainFrame, text="Breadth/Width:  ", font=("TkDefaultFont", 20))
    self.breadthTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.breadthEntry = ttk.Entry(self.mainFrame, width=20, font=("TkDefaultFont", 12))
    self.breadthEntry.grid(row=0, column=1)
    self.lengthTxt = WrappingLabel(self.mainFrame, text="Length:  ", font=("TkDefaultFont", 20))
    self.lengthTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.lengthEntry = ttk.Entry(self.mainFrame, width=20, font=("TkDefaultFont", 12))
    self.lengthEntry.grid(row=1, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=2, column=0,pady=10, padx=2, sticky="e")

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3,padx=2)

def Circle(self):
    def getInputs(self):
        answer = "Ensure that both values, i.e. Breadth/Width and Length, are numbers"
        length = str(self.lengthEntry.get())
        breadth = str(self.breadthEntry.get())
        if re.match("^\d+?\.{0,1}\d+?$", length) and re.match("^\d+?\.{0,1}\d+?$", breadth):
            print("came ")
            answer = float(length)*float(breadth)
        setFinalResult(self, answer)
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Rectangle/Square Area Calculator", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.breadthTxt = WrappingLabel(self.mainFrame, text="Breadth/Width:  ", font=("TkDefaultFont", 20))
    self.breadthTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.breadthEntry = ttk.Entry(self.mainFrame, width=20, font=("TkDefaultFont", 12))
    self.breadthEntry.grid(row=0, column=1)
    self.lengthTxt = WrappingLabel(self.mainFrame, text="Length:  ", font=("TkDefaultFont", 20))
    self.lengthTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.lengthEntry = ttk.Entry(self.mainFrame, width=20, font=("TkDefaultFont", 12))
    self.lengthEntry.grid(row=1, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=2, column=0,pady=10, padx=2, sticky="e")
    
    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3,padx=2)

def IonicEqn(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = ionicEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Ionic Equation Solver", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=("TkDefaultFont", 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=("TkDefaultFont", 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=("TkDefaultFont", 12))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def IonicEqn(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = ionicEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Ionic Equation Solver", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=("TkDefaultFont", 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=("TkDefaultFont", 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=("TkDefaultFont", 12))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def SaltSolubility(self):
    # Input Data
    def getInputs(self):
        compound = self.inputField.get()
        codeReturned = saltSolubilities(compound) # Could return error/final value
        if codeReturned:
            codeReturned = "Soluble in Water"
        else:
            codeReturned = "Insoluble in Water"
        setFinalResult(self, codeReturned)

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Salt Solubilities", font=("TkDefaultFont",50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter a Compound and the program will return an output if it is Soluble or Insoluble in water.", font=("TkDefaultFont", 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=("TkDefaultFont", 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=("TkDefaultFont", 12))
    self.inputField.insert(0, "NaCl")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=("TkDefaultFont", 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
