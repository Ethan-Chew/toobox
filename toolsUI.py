
import tkinter as tk
from tkinter import ttk
import re
import math

import string

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

numberOfDecimals = 3

#Jerick
def reload():
    '''reloads font multiplier'''
    global fontMultiplier

    try:
        file = open(jsonData)
        extractedData = json.load(file)
        file.close()
        fontMultiplier = float(extractedData["fontMultiplier"])
    except:
        with open(jsonData,"w") as f:
            tempJSON = {"fontMultiplier": float(1), "recentlyOpened": [], "default-theme": "dark"}
            json.dump(tempJSON, f)
            
reload()
newfv=int(fontMultiplier)

# Granwyn
def Prism(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical and/or fit the correct formats stated"
        volume = "-"
        surfacearea = ""
        height = str(self.he.get())
        if self.typebox.get() == "Cube":
            length = str(self.le.get())
            if re.search("^\d+\.{0,1}\d*$", length):
                volume = float(float(length)**3)
                surfacearea = 6.0*float(float(length)**2)
        elif re.search("^\d+\.{0,1}\d*$", height):
            if self.typebox.get() == "Cuboid":
                length = str(self.le.get())
                breadth = str(self.be.get())
                if re.search("^\d+\.{0,1}\d*$", length) and re.search("^\d+\.{0,1}\d*$", breadth):
                    volume = float(float(length)*float(breadth)*float(height))
                    surfacearea = 2.0*float(float(float(length)*float(breadth))+float(float(length)*float(height))+float(float(breadth)*float(height)))
            elif self.typebox.get() == "Triangular Prism":
                side1 = str(self.s1e.get())
                side2 = str(self.s2e.get())
                side3 = str(self.s3e.get())
                base_base = str(self.basee.get())
                base_height = str(self.heighte.get())
                if (bool(re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3)) ^ bool(re.search("^\d+\.{0,1}\d*$", base_base) and re.search("^\d+\.{0,1}\d*$", base_height))):
                    if re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3):
                        semiperimeter = float(float(side1)+float(side2)+float(side3))/2.0
                        volume = float(height)*float(semiperimeter*float(semiperimeter-float(side1))*(semiperimeter-float(side2))*(semiperimeter-float(side3)))**0.5
                        surfacearea = "-"
                    elif re.search("^\d+\.{0,1}\d*$", base_base) and re.search("^\d+\.{0,1}\d*$", base_height):
                        volume = float(0.5*float(base_base)*float(base_height))*float(height)
                        surfacearea = "-"
            elif self.typebox.get() == "Cylinder":
                radius = str(self.rade.get())
                diameter = str(self.diae.get())
                circumference = str(self.diae.get())
                if ((True if str(type(re.search("^\+\.{0,1}\d*$", radius))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\+\.{0,1}\d*$", diameter))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\+\.{0,1}\d*$", circumference))) != "<class 'NoneType'>" else False)):
                    if re.search("^\d+\.{0,1}\d*$", radius):
                        volume = float(height)*float(math.pi*float(radius)*float(height))
                        circumference = float(2.0*math.pi*float(radius))
                        surfacearea = float(2.0*float(math.pi*float(radius)*float(height)))+float(circumference*float(height))
                    elif re.search("^\d+\.{0,1}\d*$", diameter):
                        radius = float(diameter)/2.0
                        circumference = float(2.0*math.pi*float(radius))
                        volume = float(height)*math.pi*float(radius)*float(radius)
                        surfacearea = float(2.0*math.pi*float(radius)*float(height))+float(circumference*float(height))
        if volume != "" and surfacearea != "":
            answer = "Volume: {} u³\nSurface Area: {} {}".format(volume, surfacearea, "u²" if surfacearea != "-" else "")
        setFinalResult(self, answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Prism Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Numerical Width and Length, and Vertical Height", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    # Rectangle and Square Cross-Section
    self.bt = WrappingLabel(self.mainFrame, text="Cross-Sectional Width:  ", font=(font,int(fontMultiplier*20)))
    self.be = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.lt = WrappingLabel(self.mainFrame, text="Cross-Sectional Length:  ", font=(font,int(fontMultiplier*20)))
    self.le = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Triangle Cross-Section
    self.s1t = WrappingLabel(self.mainFrame, text="Cross-Sectional Side 1:  ", font=(font,int(fontMultiplier*20)))
    self.s1e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s2t = WrappingLabel(self.mainFrame, text="Cross-Sectional Side 2:  ", font=(font,int(fontMultiplier*20)))
    self.s2e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s3t = WrappingLabel(self.mainFrame, text="Cross-Sectional Side 3:  ", font=(font,int(fontMultiplier*20)))
    self.s3e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.baset = WrappingLabel(self.mainFrame, text="Cross-Sectional Base:  ", font=(font,int(fontMultiplier*20)))
    self.basee = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.heightt = WrappingLabel(self.mainFrame, text="Cross-Sectional Height:  ", font=(font,int(fontMultiplier*20)))
    self.heighte = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Cylinder
    self.radt = WrappingLabel(self.mainFrame, text="Cross-Sectional Radius:  ", font=(font,int(fontMultiplier*20)))
    self.rade = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.diat = WrappingLabel(self.mainFrame, text="Cross-Sectional Diameter:  ", font=(font,int(fontMultiplier*20)))
    self.diae = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Prism Height
    self.ht = WrappingLabel(self.mainFrame, text="Height:  ", font=(font,int(fontMultiplier*20)))
    self.he = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    
    # Calculate Button
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=7, column=1, padx=2, sticky="w")
    self.stuffToDelete = []

    def changeTypebox(self):
        for i in self.stuffToDelete:
            i.grid_forget()
        if self.typebox.get() == "Cuboid":
            self.infoLabel.config(text="Accepts Numerical Cross-Sectional Width and Cross-Sectional Length, and Height")
            self.bt.grid(row=1, column=0, padx=2, sticky="e")
            self.be.grid(row=1, column=1, sticky="w")
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.ht.grid(row=6, column=0, padx=2, sticky="e")
            self.he.grid(row=6, column=1, sticky="w")
            self.stuffToDelete.extend([self.bt, self.be, self.lt, self.le, self.ht, self.he])
        elif self.typebox.get() == "Cube":
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.stuffToDelete.extend([self.lt, self.le])
            self.infoLabel.config(text="Accepts Numerical Cross-Sectional Length")
        elif self.typebox.get() == "Triangular Prism":
            self.infoLabel.config(text="Accepts Numerical ((Cross-Sectional Side 1 + Cross-Sectional Side 2 + Cross-Sectional Side 3) or (Cross-Sectional Base of Triangle + Cross-Sectional Height of Triangle)) and Height")
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
            self.ht.grid(row=6, column=0, padx=2, sticky="e")
            self.he.grid(row=6, column=1, sticky="w")
            self.stuffToDelete.extend([self.s1t, self.s1e, self.s2t, self.s2e, self.s3t, self.s3e, self.baset, self.basee, self.heightt, self.heighte, self.ht, self.he])
        elif self.typebox.get() == "Cylinder":
            self.infoLabel.config(text="Accepts Numerical Cross-Sectional Radius or Cross-Sectional Diameter")
            self.radt.grid(row=1, column=0, padx=2, sticky="e")
            self.rade.grid(row=1, column=1, sticky="w")
            self.diat.grid(row=2, column=0, padx=2, sticky="e")
            self.diae.grid(row=2, column=1, sticky="w")
            self.ht.grid(row=6, column=0, padx=2, sticky="e")
            self.he.grid(row=6, column=1, sticky="w")
            self.stuffToDelete.extend([self.radt, self.rade, self.diat, self.diae, self.ht, self.he])
        self.infoLabel.pack_forget()
        self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Cube", "Cuboid", "Triangular Prism", "Cylinder"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.bind('<<ComboboxSelected>>', lambda *args: changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    changeTypebox(self)
    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:\n{}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=8,column=1,padx=2,columnspan=4, sticky="w")

# Created by Ethan
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
    self.sendData.grid(row=1, column=0, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 8, sticky = tk.W+tk.E, padx=2)

# Created by Ethan
def infoFrame(self, lblText):
    # Top Labels
    self.thingFrame = self.addframe()
    self.thingFrame.place(anchor="center", relx=0.5, rely=0.5)
    self.wipText = WrappingLabel(self.thingFrame, text=lblText, font=(font,int(fontMultiplier*30), 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = WrappingLabel(self.thingFrame, text="This is a header! Click on any 'Child' Element to access it!", font=(font,int(fontMultiplier*20)), justify="center")
    self.wipTextA.pack(side="top", pady=2)

# Ethan
def Sphere(self):
    def getInputs(self):
        answer = "Ensure that the Radius is numerical"
        radius = str(self.radiusEntry.get())
        if re.search("^\d+\.{0,1}\d*$", radius): # Validate that Answer is an Integer
            answer = sphere(radius)
        setFinalResult(answer)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Sphere Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Takes in the Radius of the Sphere as a number in UNITS (u).", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.radiusTxt = WrappingLabel(self.mainFrame, text="Radius:  ", font=(font,int(fontMultiplier*20)))
    self.radiusTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.radiusEntry = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.radiusEntry.grid(row=0, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=1, column=1, padx=2, sticky="w",pady=3)

    def setFinalResult(answer):
        try:
            self.infoTxt.grid_forget()
            self.volumeTxt.grid_forget()
            self.surfAreaTxt.grid_forget()
        except: pass
        if type(answer) == str:
            self.infoTxt = WrappingLabel(self.mainFrame, text=answer, font=(font,int(fontMultiplier*20)))
            self.infoTxt.grid(row=2,column=1,padx=2,columnspan=4, sticky="w")
        else:
            self.volumeTxt = WrappingLabel(self.mainFrame, text="Volume:  {}{}".format(answer[0], "u³"), font=(font,int(fontMultiplier*20)))
            self.volumeTxt.grid(row=2,column=1,padx=2,columnspan=4, sticky="w")
            self.surfAreaTxt = WrappingLabel(self.mainFrame, text="Surface Area:  {}{}".format(answer[1], "u²"), font=(font,int(fontMultiplier*20)))
            self.surfAreaTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w", pady=3)

#granwyn
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
        setFinalResult(self, " ".join([str(answer), "u²"]) if answer != "Ensure that all value(s) are/is numerical and/or fit the correct formats stated" else answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Parallelogram Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Numerical Base and Height", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
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
    self.sendData.grid(row=2, column=1, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3,column=1,padx=2,columnspan=4, sticky="w")
        
#granwyn
def Rectangle(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical and/or fit the correct formats stated"
        length = str(self.lengthEntry.get())
        breadth = str(self.breadthEntry.get())
        if self.typebox.get() == "Rectangle":
            if re.search("^\d+\.{0,1}\d*$", length) and re.search("^\d+\.{0,1}\d*$", breadth):
                answer = float(length)*float(breadth)
        elif self.typebox.get() == "Square":
            if re.search("^\d+\.{0,1}\d*$", length):
                answer = float(length)**2
        setFinalResult(self, " ".join([str(answer), "u²"]) if answer != "Ensure that all value(s) are/is numerical and/or fit the correct formats stated" else answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Rectangle/Square Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Numerical (Length and Breadth) or Length", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
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
    self.sendData.grid(row=3, column=1, padx=2, sticky="w")

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
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.bind('<<ComboboxSelected>>', lambda *args: changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    
    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")
        
#granwyn
def Trapezium(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical and/or fit the correct formats stated"
        t = str(self.tEntry.get())
        b = str(self.bEntry.get())
        h = str(self.hEntry.get())
        if re.search("^\d+\.{0,1}\d*$", t) and re.search("^\d+\.{0,1}\d*$", b) and re.search("^\d+\.{0,1}\d*$", h):
            answer = trapezium(t, b, h)
        setFinalResult(self, " ".join([str(answer), "u²"]) if answer != "Ensure that all value(s) are/is numerical and/or fit the correct formats stated" else answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Trapezium Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Numerical Top, Bottom and Height Lengths", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
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
    self.sendData.grid(row=3, column=1, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")
        
#granwyn
def Pyramid(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical and/or fit the correct formats stated"
        height = str(self.he.get())
        basearea = ""
        volume = ""
        if re.search("^\d+\.{0,1}\d*$", height):
            if self.typebox.get() == "Rectangular-Based Pyramid":
                length = str(self.le.get())
                breadth = str(self.be.get())
                print(length, re.search("^\d+\.{0,1}\d*$", length))
                print(breadth, re.search("^\d+\.{0,1}\d*$", breadth))
                if re.search("^\d+\.{0,1}\d*$", length) and re.search("^\d+\.{0,1}\d*$", breadth):
                    print("here")
                    basearea = float(float(length)*float(breadth))
            elif self.typebox.get() == "Square-Based Pyramid":
                length = str(self.le.get())
                if re.search("^\d+\.{0,1}\d*$", length):
                    basearea = float(float(length)*float(length))
            elif self.typebox.get() == "Triangle-Based Pyramid":
                print("hihi")
                side1 = str(self.s1e.get())
                side2 = str(self.s2e.get())
                side3 = str(self.s3e.get())
                base_base = str(self.basee.get())
                base_height = str(self.heighte.get())
                if (bool(re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3)) ^ bool(re.search("^\d+\.{0,1}\d*$", base_base) and re.search("^\d+\.{0,1}\d*$", base_height))):
                    if re.search("^\d+\.{0,1}\d*$", side1) and re.search("^\d+\.{0,1}\d*$", side2) and re.search("^\d+\.{0,1}\d*$", side3):
                        semiperimeter = float(float(side1)+float(side2)+float(side3))/2.0
                        basearea = float(semiperimeter*float(semiperimeter-float(side1))*(semiperimeter-float(side2))*(semiperimeter-float(side3)))**0.5
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
                volume = (basearea * float(height))/3.0
        if volume != "":
            answer = "Volume: {} u³".format(volume)
        setFinalResult(self, answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Pyramid Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Accepts Numerical Base Width and Base Length, and Vertical Height", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    # Rectangle and Square Based
    self.bt = WrappingLabel(self.mainFrame, text="Base Width:  ", font=(font,int(fontMultiplier*20)))
    self.be = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.lt = WrappingLabel(self.mainFrame, text="Base Length:  ", font=(font,int(fontMultiplier*20)))
    self.le = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    # Triangle Based
    self.s1t = WrappingLabel(self.mainFrame, text="Base Side 1:  ", font=(font,int(fontMultiplier*20)))
    self.s1e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s2t = WrappingLabel(self.mainFrame, text="Base Side 2:  ", font=(font,int(fontMultiplier*20)))
    self.s2e = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.s3t = WrappingLabel(self.mainFrame, text="Base Side 3:  ", font=(font,int(fontMultiplier*20)))
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
    self.sendData.grid(row=7, column=1, padx=2, sticky="w")
    self.stuffToDelete = []

    def changeTypebox(self):
        for i in self.stuffToDelete:
            i.grid_forget()
        if self.typebox.get() == "Rectangular-Based Pyramid":
            self.infoLabel.config(text="Accepts Numerical Base Width and Base Length, and Vertical Height")
            self.bt.grid(row=1, column=0, padx=2, sticky="e")
            self.be.grid(row=1, column=1, sticky="w")
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.stuffToDelete.extend([self.bt, self.be, self.lt, self.le])
        elif self.typebox.get() == "Square-Based Pyramid":
            self.lt.grid(row=2, column=0, padx=2, sticky="e")
            self.le.grid(row=2, column=1, sticky="w")
            self.stuffToDelete.extend([self.lt, self.le])
            self.infoLabel.config(text="Accepts Numerical Base Length and Vertical Height")
        elif self.typebox.get() == "Triangle-Based Pyramid":
            self.infoLabel.config(text="Accepts Numerical ((Base Side 1 + Base Side 2 + Base Side 3) or (Base of Triangle on Base + Height of Triangle on Base)) and Vertical Height")
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
            self.infoLabel.config(text="Accepts Numerical Base Circumference or Base Radius or Base Diameter")
            self.radt.grid(row=1, column=0, padx=2, sticky="e")
            self.rade.grid(row=1, column=1, sticky="w")
            self.diat.grid(row=2, column=0, padx=2, sticky="e")
            self.diae.grid(row=2, column=1, sticky="w")
            self.cirt.grid(row=3, column=0, padx=2, sticky="e")
            self.cire.grid(row=3, column=1, sticky="w")
            self.stuffToDelete.extend([self.radt, self.rade, self.diat, self.diae, self.cirt, self.cire])
        self.infoLabel.pack_forget()
        self.infoLabel.pack(side="top", fill="x", expand="yes")
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, sticky="e")
    self.types = ["Square-Based Pyramid", "Rectangular-Based Pyramid", "Triangle-Based Pyramid", "Cone"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.bind('<<ComboboxSelected>>', lambda *args: changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    self.ht.grid(row=6, column=0, padx=2, sticky="e")
    self.he.grid(row=6, column=1, sticky="w")
    changeTypebox(self)
    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:\n{}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=8,column=1,padx=2,columnspan=4, sticky="w")
        
#granwyn
def Circle(self):
    def getInputs(self):
        try:
            self.resultTxt.grid_forget()
        except: pass
        answer = "Ensure that all value(s) are/is numerical and/or fit the correct formats stated"
        c = str(self.ce.get())
        r = str(self.re.get())
        a = str(self.angle.get())
        if ((True if str(type(re.search("^\d+\.{0,1}\d*$", c))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\d+\.{0,1}\d*$", r))) != "<class 'NoneType'>" else False)) or (type(re.search("^\d+\.{0,1}\d*$", r)) and type(re.search("^\d+\.{0,1}\d*$", a))):
            if self.typebox.get() == "Semicircle":
                if re.search("^\d+\.{0,1}\d*$", r):
                    answer = float(circle(r))/float(2)
            if self.typebox.get() == "Circle":
                if bool(re.search("^\d+\.{0,1}\d*$", r)) ^ bool(re.search("^\d+\.{0,1}\d*$", c)):
                    if re.search("^\d+\.{0,1}\d*$", r):
                        answer = circle(r)
                    elif re.search("^\d+\.{0,1}\d*$", c):
                        answer = circle(float(float(c)/math.pi/float(2)))
            elif self.typebox.get() == "Sector":
                if re.search("^\d+\.{0,1}\d*$", a) and re.search("^\d+\.{0,1}\d*$", r):
                    if float(a) >= 0.0 and float(a) <= 360.0:
                        answer = sector(r, a)
        setFinalResult(self, " ".join([str(answer), "u²"]) if answer != "Ensure that all value(s) are/is numerical and/or fit the correct formats stated" else answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Circle/Semicircle Area Calculator", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="", font=(font,int(fontMultiplier*15)))
    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.ct = WrappingLabel(self.mainFrame, text="Circumference:  ", font=(font,int(fontMultiplier*20)))
    self.ce = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.rt = WrappingLabel(self.mainFrame, text="Radius:  ", font=(font,int(fontMultiplier*20)))
    self.re = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.at = WrappingLabel(self.mainFrame, text="Angle:  ", font=(font,int(fontMultiplier*20)))
    self.angle = ttk.Entry(self.mainFrame, width=20, font=(font,int(fontMultiplier*12)))
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font,int(fontMultiplier*20)))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Circle", "Semicircle", "Sector"]
    
    self.stuffToDelete = []
    def changeTypebox(self):
        for i in self.stuffToDelete:
            i.grid_forget()
        if self.typebox.get() == "Circle":
            self.ct.grid(row=1, column=0, padx=2, sticky="e")
            self.ce.grid(row=1, column=1, padx=2, sticky="w")
            self.rt.grid(row=2, column=0, padx=2, sticky="e")
            self.re.grid(row=2, column=1, padx=2, sticky="w")
            self.stuffToDelete.extend([self.ct, self.ce, self.rt, self.re])
            self.infoLabel.config(text="Accepts Numerical Radius or Circumference")
        elif self.typebox.get() == "Semicircle":
            self.rt.grid(row=2, column=0, padx=2, sticky="e")
            self.re.grid(row=2, column=1, padx=2, sticky="w")
            self.stuffToDelete.extend([self.rt, self.re])
            self.infoLabel.config(text="Accepts Numerical Radius")
        elif self.typebox.get() == "Sector":
            self.rt.grid(row=2, column=0, padx=2, sticky="e")
            self.re.grid(row=2, column=1, padx=2, sticky="w")
            self.at.grid(row=3, column=0, padx=2, sticky="e")
            self.angle.grid(row=3, column=1, padx=2, sticky="w")
            self.stuffToDelete.extend([self.rt, self.re, self.at, self.angle])
            self.infoLabel.config(text="Accepts Numerical Radius, and 0° ≤ Angle ≤ 360°")
        self.infoLabel.pack_forget()
        self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.bind('<<ComboboxSelected>>', lambda *args: changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    changeTypebox(self)
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=4, column=1, padx=2, sticky="w")

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:\n{}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=5,column=1,padx=2,columnspan=4, sticky="w")

# Created by Ethan
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
    self.anotherInfoLabel = WrappingLabel(self.thingFrame, text="This solver is limited to the list of Polyatomic Ions. However, it has been tested to work for O Level Chemical Equations, with some A Level Chemical Equations working as well.", font=(font,int(fontMultiplier*12)))
    self.anotherInfoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "2HCl(aq) + 2Na(s) -> 2NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Generate", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 5, sticky = tk.W+tk.E, padx=2)
        
# Created by Ethan
def SaltSolubility(self):
    # Input Data
    def getInputs(self):
        compound = self.inputField.get()
        codeReturned = saltSolubilities(compound) # Could return error/final value
        if codeReturned == True:
            codeReturned = "Soluble in Water"
        elif codeReturned == False:
            codeReturned = "Insoluble in Water"
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
    self.sendData.grid(row=1, column=0, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 4, sticky = tk.W+tk.E, padx=2)
        
#Jerick
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
    self.sendData.grid(row=1, column=0, padx=2)

    def setFinalResult(self, result):
        try:
            self.resultTxt.packforget()
        except:
            pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

# Ethan
# Some Granwyn
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
    self.sendData.grid(row=1, column=0, padx=2)

    def setFinalResult(self, result):
        clearResults(self)
        if type(result) == str:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text=result, font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        else:
            self.resultTxt2 = WrappingLabel(self.mainFrame, text="Shape of Graph:  {}".format(result[4]), font=(font,int(fontMultiplier*20)))
            self.resultTxt2.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            self.resultTxt2 = WrappingLabel(self.mainFrame, text="Completed the Square:  {}".format(result[1]), font=(font,int(fontMultiplier*20)))
            self.resultTxt2.grid(row=4, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            self.resultTxt3 = WrappingLabel(self.mainFrame, text="Turning Points:  ({}, {})".format(str(result[2].split(", ")[0]), result[2].split(", ")[1]), font=(font,int(fontMultiplier*20)))
            self.resultTxt3.grid(row=5, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            if len(result[0]) == 1:
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="X-intercept/Root:  ({}, 0.0)".format(result[0][0]), font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=6, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            else:
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="X-intercepts/Roots:  ({}, 0.0), ({} , 0.0)".format(result[0][0], result[0][1]), font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=6, columnspan = 2, sticky = tk.W+tk.E, padx=2)
            
            self.resultTxt4 = WrappingLabel(self.mainFrame, text="Y-intercept:  (0.0, {})".format(result[3]), font=(font,int(fontMultiplier*20)))
            self.resultTxt4.grid(row=7, columnspan = 2, sticky = tk.W+tk.E, padx=2)
    
    def clearResults(self):
        try:
            self.resultTxt1.grid_forget()
            self.resultTxt2.grid_forget()
            self.resultTxt3.grid_forget()
            self.resultTxt4.grid_forget()
        except: pass
        
#Jerick
# Some Granwyn
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
            self.resultTxt1.pack_forget()
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
                self.resultTxt1 = WrappingLabel(self.mainFrame, text="Valid inputs are required or no solution is found", font=(font,int(fontMultiplier*20)))
                self.resultTxt1.grid(row=row+4,
                columnspan = 10,
                sticky = tk.W+tk.E,
                padx=2)
        else:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="Please enter a valid input.", font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=row+4,
             columnspan = 10,
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
    if column<7:
        ttk.Button(self.mainFrame, text="Add Var", style='Accent.TButton', command=(lambda: rese(self,min(column+1,25))),width=10).grid(row=row+2, column=0,pady=2, padx=2, sticky = tk.W+tk.E)
    else:
        ttk.Button(self.mainFrame, text="Add Var", style='Accent.TButton', command=(lambda: rese(self,min(column+1,25))),width=10,state=tk.DISABLED).grid(row=row+2, column=0,pady=2, padx=2, sticky = tk.W+tk.E)
    if column>3:
        ttk.Button(self.mainFrame, text="Remove Var", style='Accent.TButton', command=(lambda: rese(self,max(column-1,3))),width=10).grid(row=row+2, column=2,pady=2, padx=2, sticky = tk.W+tk.E)
    else:
        ttk.Button(self.mainFrame, text="Remove Var", style='Accent.TButton', command=(lambda: rese(self,max(column-1,3))),width=10,state=tk.DISABLED).grid(row=row+2, column=2,pady=2, padx=2, sticky = tk.W+tk.E)

# Mostly by Jerick
## Ethan and Granwyn helped a little
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
                    if i.get().isalpha():
                        raise Exception("lazy time")
                    ang.append(math.radians( calculator().sol( i.get())[0].num))
                except Exception as e:
                    ang.append("?")
        sid=[]
        for i in sides:
            if i.get()=="":
                sid.append("?")
            else:
                try:
                    if i.get().isalpha():
                        raise Exception("lazy time")
                    sid.append(calculator().sol( i.get())[0].num)
                except Exception as e:
                    sid.append("?")
        print(*sid,*ang)
        answ = areaCalculation.solve_triangle(*sid,*ang)
        if type(answ) == list  :
            # it is correct.
            sida=answ[:3]
            anga=answ[3:-1]
            print(answ)
            print(sida,anga)
            for i in range(len(sides)):
                sides[i].delete(0, tk.END)
                sides[i].insert(0,str(sida[i]))
            for i in range(len(angles)):
                angles[i].delete(0, tk.END)
                angles[i].insert(0,str(math.degrees((anga[i]))))
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="Area: {} u²".format(answ[6]), font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)
        else:
            self.resultTxt1 = WrappingLabel(self.mainFrame, text="{}".format(answ.title()), font=(font,int(fontMultiplier*20)))
            self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)

    ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=onPress,width=10).grid(row=5, column=0,pady=2, padx=2)

# def triangle(self):
#     self.thingFrame = self.addframe()
#     self.mainLabel = WrappingLabel(self.thingFrame, text="Triangle Area Solver", font=(font,int(fontMultiplier*50),'bold'))
#     self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    
#     self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
#     self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter enough angles (A, B and C), or sides (a, b and c) to solve for area.", font=(font,int(fontMultiplier*15)))
#     self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes", columnspan = 5, sticky = tk.W+tk.N)
#     self.secInfo = WrappingLabel(self.thingFrame, text="Ensure to remove all the Placeholder Letters before running the program. (It will be taken as '1' if it is not removed.)", font=(font,int(fontMultiplier*14)))
#     self.secInfo.pack(side="top", pady=2, fill="x", expand="yes", columnspan = 7, sticky = tk.W+tk.N)
#     self.mainFrame = self.addframe()
#     self.mainFrame.pack(padx=25, pady=18, anchor="w")
#     self.mainFrame.pack(side="top", padx=25, pady=18, anchor="w")
#     anpos=[[4,0],[0,4],[4,4]]
#     angles=[]
#     entryText = ["B", "A", "C", "b", "a", "c"]
#     x = 0
#     for i in anpos:
#         temp=ttk.Entry(self.mainFrame, width=10, font=(font,int(fontMultiplier*12)))
#         temp.insert(0, entryText[x])
#         temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
#         angles.append(temp)
#         x += 1
#     sidpos=[[2,4],[4,2],[2,2]]
#     sides=[]
#     for i in sidpos:
#         temp=ttk.Entry(self.mainFrame, width=10, font=(font,int(fontMultiplier*12)))
#         temp.insert(0, entryText[x])
#         temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
#         sides.append(temp)
#         x += 1
#     diagpos=[[3,1],[1,3]]
#     for i in diagpos:
#         self.resultTxt1 = WrappingLabel(self.mainFrame, text="/", font=(font,int(fontMultiplier*20)))
#         self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
#     lines=[[4,1],[4,3]]
#     for i in lines:
#         self.resultTxt1 = WrappingLabel(self.mainFrame, text="-", font=(font,int(fontMultiplier*20)))
#         self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)

#     lines=[[1,4],[3,4]]
#     for i in lines:
#         self.resultTxt1 = WrappingLabel(self.mainFrame, text="|", font=(font,int(fontMultiplier*20)))
#         self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
#     def onPress():
#         try: self.resultTxt1.grid_forget()
#         except: pass
#         ang=[]
#         for i in angles:
#             if i.get()=="":
#                 ang.append("?")
#             else:
#                 try:
#                     ang.append(math.radians( calculator().sol( i.get())[0].num))
#                 except Exception as e:
#                     ang.append("?")
#         sid=[]
#         for i in sides:
#             if i.get()=="":
#                 sid.append("?")
#             else:
#                 try:
#                     sid.append(calculator().sol( i.get())[0].num)
#                 except Exception as e:
#                     sid.append("?")
#         answ = areaCalculation.solve_triangle(*sid,*ang)
#         if answ != "not possible":
#             # it is correct.
#             sida=answ[:3]
#             anga=answ[3:-1]
#             print(answ)
#             print(sida,anga)
#             for i in range(len(sides)):
#                 sides[i].delete(0, tk.END)
#                 sides[i].insert(0,str(sida[i]))
#             for i in range(len(angles)):
#                 angles[i].delete(0, tk.END)
#                 angles[i].insert(0,str(math.degrees((anga[i]))))
#             self.resultTxt1 = WrappingLabel(self.mainFrame, text="Area: {} u²".format(answ[6]), font=(font,int(fontMultiplier*20)))
#             self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)
#         else:
#             self.resultTxt1 = WrappingLabel(self.mainFrame, text="{}".format(answ.title()), font=(font,int(fontMultiplier*20)))
#             self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)

#     ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=onPress,width=10).grid(row=5, column=0,pady=2, padx=2)

#Ignore this there is nothing here to see
def snak():
    global root
    snake.init()
    root.bind("a", lambda :snake.get_inp("a"))
    
    root.bind("d", lambda :snake.get_inp("d"))
    
    root.bind("s", lambda :snake.get_inp("s"))
    
    root.bind("w", lambda :snake.get_inp("w"))
    
    while True:
        snake.update()
        
#Jerick/Ethan
def SolveCircle(self,typ=0):
    # Input Data
    def getInputs(self):
        selectedValue = typ
        ceqn = circle_equation()
        try:
            if selectedValue==0:
                result=ceqn.to_general_form(int(userinp[0].get()),int(userinp[1].get()),int(userinp[2].get()))
            else:
                result=ceqn.to_standard_form(int(userinp[0].get()),int(userinp[1].get()),int(userinp[2].get()))
        except:
            result="Error"
        #result = ceqn.mainCode(selectedValue, equation)
        if result == "Unknown Error" or result == "Error":
            setFinalResult(self, "An Unknown Error has Occured. Please check the format of the equation.")
        else:
            setFinalResult(self, result)
    def changebox(self):
        self.clearScreen()
        typ=0 if self.typebox.get()=="General Form" else 1
        SolveCircle(self,typ)
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
    self.typeTxt.grid(row=0, column=0, padx=2, pady=3)
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=["General Form", "Standard Form"], width=50)
    self.typebox.bind("<<ComboboxSelected>>",lambda *args: changebox(self))
    self.typebox.current(typ)
    self.typebox.grid(row=0, column=1,padx=2,columnspan=4, pady=3)
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font,int(fontMultiplier*20)))
    self.inputTxt.grid(row=1, column=0, padx=2)
    userinp=[]
    if typ==0:
        WrappingLabel(self.mainFrame, text="(x + ", font=(font,int(fontMultiplier*20))).grid(row=1,column=1)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))
        userinp[-1].grid(row=1,column=2)
        WrappingLabel(self.mainFrame, text=")² + (y + ", font=(font,int(fontMultiplier*20))).grid(row=1,column=3)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))

        userinp[-1].grid(row=1,column=4)
        WrappingLabel(self.mainFrame, text=")² = ", font=(font,int(fontMultiplier*20))).grid(row=1,column=5)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))

        userinp[-1].grid(row=1,column=6)
    else:
        WrappingLabel(self.mainFrame, text="x² + y² + ", font=(font,int(fontMultiplier*20))).grid(row=1,column=1)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))
        userinp[-1].grid(row=1,column=2)
        WrappingLabel(self.mainFrame, text="x + ", font=(font,int(fontMultiplier*20))).grid(row=1,column=3)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))

        userinp[-1].grid(row=1,column=4)
        WrappingLabel(self.mainFrame, text="y + ", font=(font,int(fontMultiplier*20))).grid(row=1,column=5)
        userinp.append(ttk.Entry(self.mainFrame,font=(font,int(fontMultiplier*12))))

        userinp[-1].grid(row=1,column=6)
        WrappingLabel(self.mainFrame, text=" = 0", font=(font,int(fontMultiplier*20))).grid(row=1,column=7)

    self.sendData = ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=2, column=0, padx=2)

    def setFinalResult(self, result):
        try: self.resultTxt.grid_forget()
        except: pass
        self.resultTxt = WrappingLabel(self.mainFrame, text="Result:  {}".format(result), font=(font,int(fontMultiplier*20)))
        self.resultTxt.grid(row=3, columnspan = 7, sticky = tk.W+tk.N, padx=2)
        
#Jerick/Granwyn
# A bit ethan
def periodicTable(self):
    def getInputs(self):
        try:
            text.pack_forget()
        except: pass
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
            text = WrappingLabel(self.mainFrame, text="Invalid Input. Please use an actual letter and number found in the Periodic Table.", font=(font,int(fontMultiplier*14)))
            text.grid(row=1, column=0, padx=2,pady=2, sticky = tk.W+tk.E, columnspan=5)
                
        # self.resFrame.grid(row=1, column=len(l)+1, rowspan=10, columnspan=10, padx=2)
        self.resFrame.grid(row=1, column=0, rowspan=len(l)+1, columnspan=10, padx=2)

    # User Interface
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Periodic Table", font=(font,int(fontMultiplier*50),'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter a valid Symbol, Element Name, Symbol, Atomic Number, or Number of Electrons, Protons or Neutrons.", font=(font,int(fontMultiplier*15)))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font,int(fontMultiplier*12)))
    self.inputField.insert(0, "H")
    self.inputField.grid(row=0, column=0)
    self.sendData = ttk.Button(self.mainFrame, text="Search", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=0, column=1, padx=2, sticky = tk.W)
    self.resFrame = ttk.Frame(self.mainFrame)
    self.resFrame.grid(row=1, column=0, rowspan=10, columnspan=10, padx=2)
# Ethan, Granwyn
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
            tempJSON = {"fontMultiplier": float(tempVal), "recentlyOpened": extractedData['recentlyOpened'], "default-theme": extractedData['default-theme']}
            json.dump(tempJSON, file)
            file.close()
            reload()
        except Exception as err: pass
        return tempVal

    def sliderChanged(event):
        try: 
            self.fontMulTxt.configure(text="Multiplier: {}".format(getCurrValue()))
            self.thingFrame.update()
        except Exception as err: 
            pass

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

    def resetSettings(self, *args):
        with open(jsonData, 'w') as f:
            json.dump({"fontMultiplier": float(1), "recentlyOpened": [], "default-theme":"dark"},f)
        reload()

    self.resetSettingsButton = ttk.Button(self.mainFrame, text="Reset Settings", style='Accent.TButton', command=lambda: resetSettings(self))
    self.resetSettingsButton.grid(row=5, sticky = tk.W+tk.E, pady=5)
    self.shortCutHeader = WrappingLabel(self.mainFrame, text="Shortcuts", font=(font,int(fontMultiplier*20), 'bold'))
    self.shortCutHeader.grid(row=6, columnspan=2, sticky = tk.W+tk.E, pady=5)
    self.fsShortcut = WrappingLabel(self.mainFrame, text="1. Control + F -- Full Screen the App.", font=(font,int(fontMultiplier*14)))
    self.fsShortcut.grid(row=7, columnspan=2, sticky= tk.W+tk.E)
    self.ufsShortcut = WrappingLabel(self.mainFrame, text="2. Escape -- Exit Full Screen.", font=(font,int(fontMultiplier*14)))
    self.ufsShortcut.grid(row=8, columnspan=2, sticky= tk.W+tk.E)
    self.hsShortcut = WrappingLabel(self.mainFrame, text="3. Control + R -- Go back to the Home Screen.", font=(font,int(fontMultiplier*14)))
    self.hsShortcut.grid(row=9, columnspan=2, sticky= tk.W+tk.E)
    # self.fsShortcut = WrappingLabel(self.mainFrame, text="4. Command + ` -- Reset back to Default Settings.", font=(font,int(fontMultiplier*14)))
    # self.fsShortcut.grid(row=10, columnspan=2, sticky= tk.W+tk.E)
