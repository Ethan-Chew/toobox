import string

import tkinter as tk
from tkinter import ttk
import re
import math
from tkinter.filedialog import dialogstates

from sympy import root
from tools import snake
from tools import areaCalculation
from tools.circleEqn import circle_equation
from tools.IonicEqn import ionicEqn
from tools.calculator import calculator
from tools.balancingChemEqn import balanceChemEqn
from components.wrappedLabel import WrappingLabel
from tools.saltSolubilities import saltSolubilities
from tools.solveQuad import solveQuad
from tools.areaCalculation import *
from tools.sim_eqn import *
import tools.periodicTable as pt
import math
import json
import os

font="TkDefaultFont"
ROOTDIR, _ =os.path.split(os.path.abspath(os.path.realpath(__file__)))
jsonData=os.path.join(ROOTDIR,".data.json")
trianglePng = os.path.join(ROOTDIR,'src','images','triangle.png')

fontMultiplier = 1.00

def reload():
    '''reloads font multiplier'''
    global fontMultiplier
    file = open(jsonData)
    extractedData = json.load(file)
    file.close()
    fontMultiplier = float(extractedData["fontMultiplier"])

reload()
newfv=int(fontMultiplier)
print(fontMultiplier)

def ChemicalEquation(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = balanceChemEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    # User Interface
    self.screenlist.append(self.addframe())
    self.thingFrame = self.screenlist[-1]
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Chemical Equation Balancer", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.screenlist.append(self.addframe())
    self.mainFrame = self.screenlist[-1]
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 5, sticky = tk.W+tk.E, padx=2)

def infoFrame(self, lblText):
    # for headers
    # Top Labels
    self.thingFrame = self.addframe()
    # self.mainLabel = WrappingLabel(self.thingFrame, text="Simultaneous Equations Solver", font=(font,int(fontMultiplier*50),'bold'))
    # self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.thingFrame.place(anchor="center", relx=0.5, rely=0.5)
    self.wipText = WrappingLabel(self.thingFrame, text=lblText, font=(font,int(fontMultiplier*30), 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = WrappingLabel(self.thingFrame, text="This is a header! Click on any 'Child' Element to access it!", font=(font,int(fontMultiplier*20)), justify="center")
    self.wipTextA.pack(side="top", pady=2)

def Parallelogram(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that both values, i.e. Breadth/Width and Length, or Length, are/is numerical"
        base = str(self.bEntry.get())
        height = str(self.hEntry.get())
        if re.search("^\d+\.{0,1}\d*$", base) and re.search("^\d+\.{0,1}\d*$", height):
            answer = parallelogram(base, height)
        setFinalResult(self, " ".join([str(answer), "u²"]))
    self.thingFrame =self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Parallelogram Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.bTxt = WrappingLabel(self.mainFrame, text="Base:  ", font=(font,int(fontMultiplier*20)))
    self.bTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.bEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.bEntry.grid(row=0, column=1, sticky="w")
    self.hTxt = WrappingLabel(self.mainFrame, text="Height:  ", font=(font,int(fontMultiplier*20)))
    self.hTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.hEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.hEntry.grid(row=1, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=2, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3,column=1,padx=2,columnspan=4, sticky="w")
def Rectangle(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical"
        length = str(self.lengthEntry.get())
        breadth = str(self.breadthEntry.get())
        if self.typebox.get() == "Rectangle":
            if re.search("^\d+\.{0,1}\d*$", length) and re.search("^\d+\.{0,1}\d*$", breadth):
                answer = float(length)*float(breadth)
        elif self.typebox.get() == "Square":
            if re.search("^\d+\.{0,1}\d*$", length):
                answer = float(length)**2
        setFinalResult(self, " ".join([str(answer), "u²"]))
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Rectangle/Square Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.breadthTxt = WrappingLabel(self.mainFrame, text="Breadth/Width:  ", font=(font,int(fontMultiplier*20)))
    self.breadthTxt.grid(row=2, column=0, padx=2, sticky="e")
    self.breadthEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.breadthEntry.grid(row=2, column=1, sticky="w")
    self.lengthTxt = WrappingLabel(self.mainFrame, text="Length:  ", font=(font,int(fontMultiplier*20)))
    self.lengthTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.lengthEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.lengthEntry.grid(row=1, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=3, column=1, pady=10, padx=2, sticky="w")

    def changeTypebox(self):
        if self.typebox.get() == "Square":
            self.breadthTxt.grid_forget()
            self.breadthEntry.grid_forget()
        else:
            self.breadthTxt.grid(row=2, column=0, padx=2, sticky="e")
            self.breadthEntry.grid(row=2, column=1, sticky="w")

    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Rectangle", "Square"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types, postcommand=lambda:changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    
    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")

def Trapezium(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical"
        t = str(self.tEntry.get())
        b = str(self.bEntry.get())
        h = str(self.hEntry.get())
        if re.search("^\d+\.{0,1}\d*$", t) and re.search("^\d+\.{0,1}\d*$", b) and re.search("^\d+\.{0,1}\d*$", h):
            answer = trapezium(t, b, h)
        setFinalResult(self, " ".join([str(answer), "u²"]))
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Trapezium Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.tTxt = WrappingLabel(self.mainFrame, text="Top:  ", font=(font,int(fontMultiplier*20)))
    self.tTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.tEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.tEntry.grid(row=0, column=1, sticky="w")
    self.bTxt = WrappingLabel(self.mainFrame, text="Bottom:  ", font=(font,int(fontMultiplier*20)))
    self.bTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.bEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.bEntry.grid(row=1, column=1, sticky="w")
    self.hTxt = WrappingLabel(self.mainFrame, text="Height:  ", font=(font,int(fontMultiplier*20)))
    self.hTxt.grid(row=2, column=0, padx=2, sticky="e")
    self.hEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.hEntry.grid(row=2, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=3, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")

def Pyramid(self):
    comboboxText = ""
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical"
        height = str(self.he.get())
        basearea = ""
        if re.search("^\d+\.{0,1}\d*$", height):
            if self.typebox.get() == "Rectangle-Based Pyramid":
                length = str(self.le.get())
                breadth = str(self.be.get())
                if re.search("^\d+\.{0,1}\d*$", length) and re.search("^\d+\.{0,1}\d*$", breadth):
                    basearea = float(float(length)*float(breadth))
            elif self.typebox.get() == "Square-Based Pyramid":
                length = str(self.le.get())
                if re.search("^\d+\.{0,1}\d*$", length):
                    basearea = float(float(length)*float(length))
            elif self.typebox.get() == "Triangle-Based Pyramid":
                side1 = str(self.s1e.get())
                side2 = str(self.s2e.get())
                side3 = str(self.s3e.get())
                base_base = str(self.basee.get())
                base_height = str(self.heighte.get())
                if ((re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3)) ^ (re.search("^\d+\.{0,1}\d*$", base_base) and re.search("^\d+\.{0,1}\d*$", base_height))):
                    if re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3):
                        semiperimeter = float(float(side1)+float(side2)+float(side3))/2
                        basearea = float(semiperimeter*(semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))**0.5
                    elif re.search("^\d+\.{0,1}\d*$", base_base) and re.search("^\d+\.{0,1}\d*$", base_height):
                        basearea = 0.5*float(base_base)*float(base_height)
            elif self.typebox.get() == "Cone":
                radius = str(self.rade.get())
                diameter = str(self.diae.get())
                circumference = str(self.diae.get())
                if ((True if str(type(re.search("^\+\.{0,1}\d*$", radius))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\+\.{0,1}\d*$", diameter))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\+\.{0,1}\d*$", circumference))) != "<class 'NoneType'>" else False)):
                    if re.search("^\d+\.{0,1}\d*$", radius):
                        basearea = math.pi*float(radius)**2
                    elif re.search("^\d+\.{0,1}\d*$", diameter):
                        basearea = math.pi*float(float(diameter)/2.0)**2
                    elif re.search("^\d+\.{0,1}\d*$", circumference):
                        basearea = math.pi*float(float(float(circumference)/math.pi)/2.0)**2
                # (True if str(type(re.search("^\+\.{0,1}\d*$", r))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\d+\.{0,1}\d*$", c))
            if type(basearea) == float:
                answer = (basearea * float(height))/3
        setFinalResult(self, " ".join([str(answer), "u²"]) if answer != "Ensure that all value(s) are/is numerical" else answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Pyramid Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Base Width and Base Length", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    # Rectangle and Square Based
    self.bt = WrappingLabel(self.mainFrame, text="Base Width:  ", font=(font,int(fontMultiplier*20)))
    self.be = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.lt = WrappingLabel(self.mainFrame, text="Base Length:  ", font=(font,int(fontMultiplier*20)))
    self.le = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Triangle Based
    self.s1t = WrappingLabel(self.mainFrame, text="Side 1:  ", font=(font,int(fontMultiplier*20)))
    self.s1e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s2t = WrappingLabel(self.mainFrame, text="Side 2:  ", font=(font,int(fontMultiplier*20)))
    self.s2e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s3t = WrappingLabel(self.mainFrame, text="Side 3:  ", font=(font,int(fontMultiplier*20)))
    self.s3e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.baset = WrappingLabel(self.mainFrame, text="Base:  ", font=(font,int(fontMultiplier*20)))
    self.basee = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.heightt = WrappingLabel(self.mainFrame, text="Height:  ", font=(font,int(fontMultiplier*20)))
    self.heighte = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Cone
    self.radt = WrappingLabel(self.mainFrame, text="Base Radius:  ", font=(font,int(fontMultiplier*20)))
    self.rade = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.diat = WrappingLabel(self.mainFrame, text="Base Diameter:  ", font=(font,int(fontMultiplier*20)))
    self.diae = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.cirt = WrappingLabel(self.mainFrame, text="Base Circumference:  ", font=(font,int(fontMultiplier*20)))
    self.cire = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Pyramid Height
    self.ht = WrappingLabel(self.mainFrame, text="Vertical Height:  ", font=(font,int(fontMultiplier*20)))
    self.he = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    
    # Calculate Button
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=7, column=1, pady=10, padx=2, sticky="w")
    self.stuffToDelete = []

    def changeTypebox(self):
        for i in self.stuffToDelete:
            i.grid_forget()
        if self.typebox.get() == "Rectangular-Based Pyramid":
            self.infoLabel.config(text="Accepts Base Width and Base Length")
            self.bt.grid(row=1, column=0, padx=2, sticky="e")
            self.be.grid(row=1, column=1, sticky="w")
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.stuffToDelete.extend([self.bt, self.be, self.lt, self.le])
        elif self.typebox.get() == "Square-Based Pyramid":
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.stuffToDelete.extend([self.lt, self.le])
        elif self.typebox.get() == "Triangle-Based Pyramid":
            self.infoLabel.config(text="Accepts (Side 1 + Side2 + Side3) OR (Base of Triangle on Base + Height of Triangle on Base")
            self.s1t.grid(row=1, column=0, padx=2, sticky="e")
            self.s1e.grid(row=1, column=1, sticky="w")
            self.s2t.grid(row=2, column=0, padx=2, sticky="e")
            self.s2e.grid(row=2, column=1, sticky="w")
            self.s3t.grid(row=3, column=0, padx=2, sticky="e")
            self.s3e.grid(row=3, column=1, sticky="w")
            self.baset.grid(row=4, column=0, padx=2, sticky="e")
            self.basee.grid(row=4, column=1, sticky="w")
            self.heightt.grid(row=5, column=0, padx=2, sticky="e")
            self.heighte.grid(row=5, column=1, sticky="w")
            self.stuffToDelete.extend([self.s1t, self.s1e, self.s2t, self.s2e, self.s3t, self.s3e, self.baset, self.basee, self.heightt, self.heighte])
        elif self.typebox.get() == "Cone":
            self.infoLabel.config(text="Accepts Base Circumference OR Base Radius OR Base Diameter")
            self.radt.grid(row=1, column=0, padx=2, sticky="e")
            self.rade.grid(row=1, column=1, sticky="w")
            self.diat.grid(row=2, column=0, padx=2, sticky="e")
            self.diae.grid(row=2, column=1, sticky="w")
            self.cirt.grid(row=3, column=0, padx=2, sticky="e")
            self.cire.grid(row=3, column=1, sticky="w")
            self.stuffToDelete.extend([self.radt, self.rade, self.diat, self.diae, self.cirt, self.cire])
        self.infoLabel.config(text="Accepts Base Length")
        self.infoLabel.pack_forget()
        self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Square-Based Pyramid", "Rectangular-Based Pyramid", "Triangle-Based Pyramid", "Cone"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    def commandTypebox(event):
        changeTypebox(self)
    self.typebox.bind('<<ComboboxSelected>>', commandTypebox)
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    self.ht.grid(row=6, column=0, padx=2, sticky="e")
    self.he.grid(row=6, column=1, sticky="w")
    changeTypebox(self)
    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=8,column=1,padx=2,columnspan=4, sticky="w")

def Circle(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical"
        r = str(self.ce.get())
        c = str(self.re.get())
        a = str(self.angle.get())
        if ((True if str(type(re.search("^\d+\.{0,1}\d*$", r))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\d+\.{0,1}\d*$", c))) != "<class 'NoneType'>" else False)) or (type(re.search("^\d+\.{0,1}\d*$", r)) and type(re.search("^\d+\.{0,1}\d*$", a))):
            if re.search("^\d+\.{0,1}\d*$", r):
                answer = circle(r)
            elif re.search("^\d+\.{0,1}\d*$", c):
                answer = circle(float(c)/math.pi/float(2))
                if self.typebox.get() == "Semicircle":
                    answer = float(answer)/float(2)
            elif self.typebox.get() == "Sector":
                if re.search("^\d+\.{0,1}\d*$", a) and re.search("^\d+\.{0,1}\d*$", r):
                    if float(a) >= 0.0 and float(a) <= 360.0:
                        answer = sector(r, a)
        setFinalResult(self, " ".join([str(answer), "u²"]))
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Circle/Semicircle Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.ct = WrappingLabel(self.mainFrame, text="Circumference:  ", font=(font,int(fontMultiplier*20)))
    self.ct.grid(row=1, column=0, padx=2, sticky="e")
    self.ce = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.ce.grid(row=1, column=1, padx=2, sticky="w")
    self.rt = WrappingLabel(self.mainFrame, text="Radius:  ", font=(font,int(fontMultiplier*20)))
    self.rt.grid(row=2, column=0, padx=2, sticky="e")
    self.re = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.re.grid(row=2, column=1, padx=2, sticky="w")
    self.at = WrappingLabel(self.mainFrame, text="Angle:  ", font=(font,int(fontMultiplier*20)))
    self.at.grid(row=3, column=0, padx=2, sticky="e")
    self.angle = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.angle.grid(row=3, column=1, padx=2, sticky="w")
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Circle", "Semicircle", "Sector"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=4, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=5,column=1,padx=2,columnspan=4, sticky="w")


def IonicEqn(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = ionicEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Ionic Equation Solver", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "2HCl(aq) + 2Na(s) -> 2NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Generate", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 5, sticky = tk.W+tk.E, padx=2)

def SaltSolubility(self):
    # Input Data
    def getInputs(self):
        compound = self.inputField.get()
        codeReturned = saltSolubilities(compound) # Could return error/final value
        if codeReturned == True:
            codeReturned = "Soluble in Water"
        elif codeReturned == False:
            codeReturned = "Insoluble in Water"
        exec("\x69\x66\x20\x63\x6F\x64\x65\x52\x65\x74\x75\x72\x6E\x65\x64\x20\x3D\x3D\x20\x22\x71\x77\x65\x72\x74\x79\x75\x69\x6F\x70\x30\x39\x38\x37\x36\x35\x34\x33\x32\x31\x68\x65\x6C\x6C\x6F\x77\x6F\x72\x6C\x64\x22\x3A\x20\x73\x65\x6C\x66\x2E\x5F\x71\x75\x69\x74\x28\x29")
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Salt Solubilities", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter a Compound and the program will return an output if it is Soluble or Insoluble in water.", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "NaCl")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Check", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 4, sticky = tk.W+tk.E, padx=2)

def calculate(self):
    # Input Data
    def getInputs(self):
        inputVal = self.inputField.get()
        #if re.search("^((\(|\))*(\d+\.{0,1}\d{0,1})+(\(|\))*(\+|\-|\*|\/)*(\(|\))*)+$", inputVal):
        final=""
        for i in inputVal:
            if i!=" ":
                final+=i
        try:
            codeReturned = str(calculator().sol(final)[0].num) # Could return error/final value
        except:
            codeReturned="error"
        # else:
        #     codeReturned = "Invalid Input"
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Enter a mathematical expression. currently, only +,-,*,/,(),^ are supported", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "9 + 10")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try:
            self.resultTxt.packforget()
        except:
            pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def SolveQuad(self):
    # Input Data
    def getInputs(self):
        eqn = self.inputField.get()
        codeReturned = solveQuad(eqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Solving Quadratic Equation", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter an Equation in the format ax^2+bx+c.", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "x^2+2x+8")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Check", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        clearResults(self)
        if type(result) == str:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text=result, font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        else:
            if len(result[0]) == 1:
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="Roots:  {}".format(result[0][0]), font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            else:
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="Roots:  {}, {}".format(result[0][0], result[0][1]), font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            self.resultTxt2 = WrappingLabel(self.mainFrame, text="Completed the Square:  {}".format(result[1]), font=(font,int(fontMultiplier*20)))
            self.resultTxt2.grid(row=4, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            self.resultTxt3 = WrappingLabel(self.mainFrame, text="Turning Points:  {}, {}".format(str(result[2].split(", ")[0]), result[2].split(", ")[1]), font=(font,int(fontMultiplier*20)))
            self.resultTxt3.grid(row=5, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            self.resultTxt4 = WrappingLabel(self.mainFrame, text="Y Intercept:  {}".format(result[3]), font=(font,int(fontMultiplier*20)))
            self.resultTxt4.grid(row=6, columnspan = 2, sticky = tk.W+tk.E, padx=2)
    
    def clearResults(self):
        try:
            self.resultTxt1.grid_forget()
            self.resultTxt2.grid_forget()
            self.resultTxt3.grid_forget()
            self.resultTxt4.grid_forget()
        except: pass

def simsolver(self,column=3):
    row=column-1

    # self.newFrame.pack(side="top", padx=25, pady=18, anchor="nw")
    self.thingFrame = self.addframe()
    self.mainLabel = WrappingLabel(self.thingFrame, text="Simultaneous Equations Solver", font=(font,int(fontMultiplier*50),'bold'))
    self.thingFrame.pack(side="top", padx=25, pady=18,anchor="w")
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.mainFrame = self.addframe()
    self.mainFrame.pack(side="top",padx=25, pady=18,anchor="nw")
    
    # self.notebook.create_window((0, 0), window=self.newFrame, anchor="nw")
    # self.scrollx = ttk.Scrollbar(self.homeScreen, orient="horizontal")
    # self.scrollx.pack(side="bottom", fill="x")
    # self.scrollx.config(command=self.notebook.xview)
    # self.scrolly = ttk.Scrollbar(self.paned, orient="vertical")
    # self.scrolly.pack(side="right", fill="y")
    # self.scrolly.config(command=self.notebook.yview)

    def gen_table(row,column):
        table=[]
        for i in range(row):
            table.append([])
            for j in range(column):
                temp=ttk.Entry(self.mainFrame, width=10, font=(font,int(fontMultiplier*12)))
                if j<column-2:
                    tempt=str(string.ascii_lowercase[j])+" + "
                elif j==column-2:
                    tempt=str(string.ascii_lowercase[j])+" = "
                else:
                    tempt=""
                self.alpha = WrappingLabel(self.mainFrame, text=tempt, font=(font,int(fontMultiplier*20)))
                self.alpha.grid(row=i, column=max(0,((j+1)*2)-1), sticky = tk.W+tk.E, padx=2)
                temp.grid(row=i,column=j*2,padx=2,pady=2, sticky = tk.W+tk.E)
                table[i].append(temp)
        # self.scrollx.config(command=self.mainFrame.xview)
        # self.scrolly.config(command=self.mainFrame.yview)
        return table
    # self.tree = ttk.Treeview(self.mainFrame, selectmode="extended")
    table=gen_table(row,column)

    # vsb = tk.Scrollbar(self.mainFrame, orient=tk.HORIZONTAL, command=self.tree.xview)
    # vsb.grid(row=0, column=0, sticky='ew')
    # self.mainFrame.configure(yscrollcommand=vsb.set)

    def onPress():
        try:
            self.resultTxt1.packforget()
        except:
            pass
        #solve_sim
        ret=[]
        can=True
        for r in table:
            ret.append([])
            for col in r:
                try:
                    ret[-1].append(calculator().sol(col.get())[0].num)
                except Exception as e:
                    can=False
        if can:
            try:
                answer=np.array(solve_sim(*ret))
                ans=""
                j=0
                for i in answer:
                    ans+=string.ascii_lowercase[j]+" = "+str(i[0][0])+"\n"
                    j+=1
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="Roots:  \n{}".format(ans), font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=row+4,
                columnspan = 2,
                sticky = tk.W+tk.E,
                padx=2)
            except:
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="Please enter a valid input.", font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=row+4,
                columnspan = 2,
                sticky = tk.W+tk.E,
                padx=2)
        else:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="Please enter a valid input.", font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=row+4,
             columnspan = 2,
             sticky = tk.W+tk.E,
             padx=2)

    def rese(self,col):
        self.thingFrame.pack_forget()
        self.mainFrame.pack_forget()
        #self.scrollx.pack_forget()
        # self.newFrame.pack_forget()
        self.clearScreen()
        simsolver(self,col)
    ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=onPress,width=10).grid(row=row+3, column=0,pady=2, padx=2)
    ttk.Button(self.mainFrame, text="Add Var", style='Accent.TButton', command=(lambda: rese(self,min(column+1,25))),width=10).grid(row=row+2, column=0,pady=2, padx=2)
    if column>3:
        ttk.Button(self.mainFrame, text="Remove Var", style='Accent.TButton', command=(lambda: rese(self,max(column-1,3))),width=10).grid(row=row+2, column=2,pady=2, padx=2)
    else:
        ttk.Button(self.mainFrame, text="Remove Var", style='Accent.TButton', command=(lambda: rese(self,max(column-1,3))),width=10,state=tk.DISABLED).grid(row=row+2, column=2,pady=2, padx=2)

def triangle(self):
    self.thingFrame = self.addframe()
    self.mainLabel = WrappingLabel(self.thingFrame, text="Triangle Area Solver", font=(font,int(fontMultiplier*50),'bold'))
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter enough angles (A, B and C), or sides (a, b and c) to solve for area", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.mainFrame.pack(side="top", padx=25, pady=18, anchor="w")
    anpos=[[4,0],[0,4],[4,4]]
    angles=[]
    entryText = ["B", "A", "C", "b", "a", "c"]
    x = 0
    for i in anpos:
        temp=ttk.Entry(self.mainFrame, width=10, font=(font,int(fontMultiplier*12)))
        temp.insert(0, entryText[x])
        temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
        angles.append(temp)
        x += 1
    sidpos=[[2,4],[4,2],[2,2]]
    sides=[]
    for i in sidpos:
        temp=ttk.Entry(self.mainFrame, width=10, font=(font,int(fontMultiplier*12)))
        temp.insert(0, entryText[x])
        temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
        sides.append(temp)
        x += 1
    diagpos=[[3,1],[1,3]]
    for i in diagpos:
        self.resultTxt1 = WrappingLabel(self.mainFrame, text="/", font=(font,int(fontMultiplier*20)))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
    lines=[[4,1],[4,3]]
    for i in lines:
        self.resultTxt1 = WrappingLabel(self.mainFrame, text="-", font=(font,int(fontMultiplier*20)))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)

    lines=[[1,4],[3,4]]
    for i in lines:
        self.resultTxt1 = WrappingLabel(self.mainFrame, text="|", font=(font,int(fontMultiplier*20)))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
    def onPress():
        try: self.resultTxt1.grid_forget()
        except: pass
        ang=[]
        for i in angles:
            if i.get()=="":
                ang.append("?")
            else:
                try:
                    ang.append(math.radians( calculator().sol( i.get())[0].num))
                except Exception as e:
                    ang.append("?")
        sid=[]
        for i in sides:
            if i.get()=="":
                sid.append("?")
            else:
                try:
                    sid.append(calculator().sol( i.get())[0].num)
                except Exception as e:
                    sid.append("?")
        answ = areaCalculation.solve_triangle(*sid,*ang)
        if answ != "not possible":
            # it is correct.
            sida=answ[:3]
            anga=answ[3:-1]
            print(answ)
            print(sida,anga)
            for i in range(len(sides)):
                sides[i].insert(0,str(sida[i]))
            for i in range(len(angles)):
                angles[i].insert(0,str(math.degrees((anga[i]))))
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="Area: {} u²".format(answ[6]), font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)
        else:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="{}".format(answ.title()), font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)

    ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=onPress,width=10).grid(row=5, column=0,pady=2, padx=2)

def snak():
    global root
    snake.init()
    root.bind("a", lambda :snake.get_inp("a"))
    
    root.bind("d", lambda :snake.get_inp("d"))
    
    root.bind("s", lambda :snake.get_inp("s"))
    
    root.bind("w", lambda :snake.get_inp("w"))
    
    while True:
        snake.update()

def SolveCircle(self):
    # Input Data
    def getInputs(self):
        equation = self.inputField.get()
        selectedValue = self.typebox.get()
        ceqn = circle_equation()
        result = ceqn.mainCode(selectedValue, equation)
        if result == "Unknown Error" or result == "Error":
            setFinalResult(self, "An Unknown Error has Occured. Please check the format of the equation.")
        else:
            setFinalResult(self, result)

    # User Interface
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Equation of Circle", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Equation in the following Formats. General Form - (x + a)^2 + (y + b)^2 = r^2, Standard Form - x^2 + y^2 + ax + by + c = 0", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.typeTxt = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typeTxt.grid(row=0, column=0, padx=2)
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=["General Form", "Standard Form"], width=50)
    self.typebox.grid(row=0, column=1,padx=2)
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=1, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "Equation")
    self.inputField.grid(row=1, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=2, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.N, padx=2)

def periodicTable(self):
    def getInputs(self):
        self.resFrame.destroy()
        self.resFrame = self.addframe(self.mainFrame)
        e = self.inputField.get().replace(" ", "")
        l=pt.search(e)[:6]
        newf=self.addframe(self.resFrame,borderwidth=1)

        if len(l) > 0: 
            temp=WrappingLabel(newf, text="Atomic Number", font=(font,int(fontMultiplier*10)))
            temp.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Mass Number", font=(font,int(fontMultiplier*10)))
            temp.grid(row=1, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Period"+", "+"Group", font=(font,int(fontMultiplier*10)))
            temp.grid(row=2, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Symbol", font=(font,int(fontMultiplier*15), 'bold'))
            temp.grid(row=3, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Element", font=(font,int(fontMultiplier*12), 'bold'))
            temp.grid(row=4, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Atomic Mass" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=5, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text=", ".join(["Protons","Neutrons","Electrons"]), font=(font,int(fontMultiplier*10)))
            temp.grid(row=6, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Atomic Radius" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=7, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electron Shells" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=8, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Valence Electrons" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=9, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electronic Configuration" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=10, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Isotopes" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=11, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text=" ".join(["[{}]".format("Phase"), ", ".join(["Melting Point", "Boiling Point"])]), font=(font,int(fontMultiplier*10)))
            temp.grid(row=12, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Type" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=13, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Radioactive" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=14, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Natural" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=15, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Density" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=16, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Electronegativity" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=17, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="First Ionisation Energy" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=18, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Specific Heat Capacity / J⋅kg⁻¹⋅K⁻¹" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=19, column=0, sticky = tk.N+tk.E, padx=2)

            temp=WrappingLabel(newf, text="Discovered" , font=(font,int(fontMultiplier*10)))
            temp.grid(row=20, column=0, sticky = tk.N+tk.E, padx=2)

            newf.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

            r=1
            for i in l:
                newf=self.addframe(self.resFrame,borderwidth=1)
                
                temp=WrappingLabel(newf, text=int(pt.ELEMENTDATA["AtomicNumber"][i]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=0, column=0, sticky = tk.N+tk.W, padx=2)
                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["MassNumber"][i])), font=(font,int(fontMultiplier*10)))
                temp.grid(row=1, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Period"][i]))+", "+str(int(pt.ELEMENTDATA["Group"][i])), font=(font,int(fontMultiplier*10)))
                temp.grid(row=2, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Symbol"][i]), font=(font,int(fontMultiplier*15), 'bold'))
                temp.grid(row=3, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Element"][i]), font=(font,int(fontMultiplier*12), 'bold'))
                temp.grid(row=4, column=0, sticky = tk.N+tk.W, padx=2)
                
                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["AtomicMass"][i]) , font=(font,int(fontMultiplier*10)))
                temp.grid(row=5, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=", ".join([str(int(pt.ELEMENTDATA[j][i])) for j in ["Protons","Neutrons","Electrons"]]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=6, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["AtomicRadius"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=7, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Shells"][i])).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=8, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(int(pt.ELEMENTDATA["Valence"][i])).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=9, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Config"][i]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=10, column=0, sticky = tk.N+tk.W, padx=2)

                iso = str(pt.ELEMENTDATA["Isotopes"][i])
                temp=WrappingLabel(newf, text=str(int(float(iso))) if iso.replace('.','',1).isdigit() else "-", font=(font,int(fontMultiplier*10)))
                temp.grid(row=11, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=" ".join(["[{}]".format(str(pt.ELEMENTDATA["Phase"][i]).title()), ", ".join([str(pt.ELEMENTDATA["MeltingPoint"][i]).title()+"K", str(pt.ELEMENTDATA["BoilingPoint"][i]).title()+"K"])]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=12, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Type"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=13, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text="Yes" if pt.ELEMENTDATA["Radioactive"][i] else "No", font=(font,int(fontMultiplier*10)))
                temp.grid(row=14, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text="Yes" if pt.ELEMENTDATA["Natural"][i] else "No", font=(font,int(fontMultiplier*10)))
                temp.grid(row=15, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["Density"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=16, column=0, sticky = tk.N+tk.W, padx=2)

                e = str(pt.ELEMENTDATA["Electronegativity"][i]).title()
                temp=WrappingLabel(newf, text=e if e.replace('.','',1).isdigit() else "-", font=(font,int(fontMultiplier*10)))
                temp.grid(row=17, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["FirstIonization"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=18, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=str(pt.ELEMENTDATA["SpecificHeat"][i]).title(), font=(font,int(fontMultiplier*10)))
                temp.grid(row=19, column=0, sticky = tk.N+tk.W, padx=2)

                temp=WrappingLabel(newf, text=", ".join([str(pt.ELEMENTDATA["Discoverer"][i]).title(), str(pt.ELEMENTDATA["Year"][i]).title()]), font=(font,int(fontMultiplier*10)))
                temp.grid(row=20, column=0, sticky = tk.N+tk.W, padx=2)

                newf.grid(row=0, column=r, sticky = tk.N, padx=2)
                r+=1
        else:
            text = WrappingLabel(newf, text="Invalid Element Input. Please use an actual letter found in the Periodic Table.", font=(font,int(fontMultiplier*12)))
            text.grid(row=0, column=0, padx=2,pady=2, sticky = tk.W+tk.E, columnspan=5)
                
        # self.resFrame.grid(row=1, column=len(l)+1, rowspan=10, columnspan=10,pady=10, padx=2)
        self.resFrame.grid(row=1, column=0, rowspan=len(l)+1, columnspan=10,pady=10, padx=2)

    # User Interface
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Periodic Table", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter a valid Symbol, Element Name, Symbol, Atomic Number, or Number of Electrons, Protons or Neutrons. To search for protons input \"Pn\" where n is the number of Protons. You can similarly search for neutrons and electorns with \"Nn\" and \"En\" respectively", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "H")
    self.inputField.grid(row=0, column=0)
    self.sendData = ttk.Button(self.mainFrame, text="Search", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=0, column=1,pady=10, padx=2, sticky = tk.W)
    self.resFrame = ttk.Frame(self.mainFrame)
    self.resFrame.grid(row=1, column=0, rowspan=10, columnspan=10,pady=10, padx=2)

def Settings(self):
    # Font Multiplier
    currentVal = tk.DoubleVar()
    
    def getCurrValue():
        
        tempVal = '{: .2f}'.format(currentVal.get()/30)
        try:
            global extractedData
            extractedData = {}
            file = open(jsonData, "r")
            extractedData = json.load(file)
            file.close()
            file = open(jsonData, "w+")
            tempJSON = {"fontMultiplier": float(tempVal), "recentlyOpened": extractedData['recentlyOpened']}
            json.dump(tempJSON, file)
            file.close()
            reload()
        except Exception as err: print(err)
        return tempVal

    def sliderChanged(event):
        try: 
            self.fontMulTxt.configure(text="Multiplier: {}".format(getCurrValue()))
            self.thingFrame.update()
        except Exception as err: 
            print(err)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Settings", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Adjust Settings of the App here", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.fontMulHeader = WrappingLabel(self.mainFrame, text="Font Multiplier", font=(font,int(fontMultiplier*20), 'bold'))
    self.fontMulHeader.grid(row=0, columnspan=2, sticky = tk.W+tk.E, pady=5)
    self.fontMulSlider = ttk.Scale(self.mainFrame, from_=0, to=160, length=400, command=sliderChanged, variable=currentVal)
    self.fontMulSlider.set(int(fontMultiplier*30))
    self.fontMulSlider.grid(row=1, pady=2, columnspan = 5, sticky = tk.W+tk.E)
    self.fontMulTxt = WrappingLabel(self.mainFrame, text="Multiplier: ", font=(font,int(fontMultiplier*12)))
    self.fontMulTxt.config(text="Multiplier: {}".format(getCurrValue()))
    self.fontMulTxt.grid(row=2, columnspan=2, sticky= tk.W+tk.E)
    self.infoLabel = WrappingLabel(self.mainFrame, text="Please restart for best results", font=(font,int(fontMultiplier*10)))
    self.infoLabel.grid(row=3, columnspan=2, sticky= tk.W+tk.E)
    self.anotherInfoLbl = WrappingLabel(self.mainFrame, text="The largest recommended Font Multiplier is 2x. Going higher may result in the User Interface being unusable.", font=(font,int(fontMultiplier*10)))
    self.anotherInfoLbl.grid(row=4, columnspan=5, sticky= tk.W+tk.E)