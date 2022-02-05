import string

import tkinter as tk
from tkinter import ttk
import re

from chemlib import Element

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
font="TkDefaultFont"

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False
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
    self.mainLabel = WrappingLabel(self.thingFrame, text="Chemical Equation Balancer", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.screenlist.append(self.addframe())
    self.mainFrame = self.screenlist[-1]
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Balance", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def infoFrame(self, lblText):
    # Top Labels
    self.thingFrame = self.addframe()
    # self.mainLabel = WrappingLabel(self.thingFrame, text="Simultaneous Equations Solver", font=(font,50,'bold'))
    # self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.thingFrame.place(anchor="center", relx=0.5, rely=0.5)
    self.wipText = WrappingLabel(self.thingFrame, text=lblText, font=(font, 30, 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = WrappingLabel(self.thingFrame, text="This is a header! Click on any 'Child' Element to access the calculator!", font=(font, 20), justify="center")
    self.wipTextA.pack(side="top", pady=2)

def Parallelogram(self):
    def getInputs(self):
        try:
            self.resultTxt.forget_grid()
            self.resultTxt.grid.forget()
        except: pass
        answer = "Ensure that both values, i.e. Breadth/Width and Length, or Length, are/is numerical"
        base = str(self.bEntry.get())
        height = str(self.hEntry.get())
        if re.search("^\d+\.{0,1}\d{0,1}$", base) and re.search("^\d+\.{0,1}\d{0,1}$", height):
            answer = parallelogram(base, height)
        setFinalResult(self, answer)
    self.thingFrame =self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Parallelogram Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.bTxt = WrappingLabel(self.mainFrame, text="Base:  ", font=(font, 20))
    self.bTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.bEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.bEntry.grid(row=0, column=1, sticky="w")
    self.hTxt = WrappingLabel(self.mainFrame, text="Height:  ", font=(font, 20))
    self.hTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.hEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.hEntry.grid(row=1, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=2, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=3,column=1,padx=2,columnspan=4, sticky="w")

def Trapezium(self):
    def getInputs(self):
        try:
            self.resultTxt.forget_grid()
            self.resultTxt.grid.forget()
        except: pass
        answer = "Ensure that both values, i.e. Breadth/Width and Length, or Length, are/is numerical"
        t = str(self.tEntry.get())
        b = str(self.bEntry.get())
        h = str(self.hEntry.get())
        if re.search("^\d+\.{0,1}\d{0,1}$", t) and re.search("^\d+\.{0,1}\d{0,1}$", b) and re.search("^\d+\.{0,1}\d{0,1}$", h):
            answer = trapezium(t, b, h)
        setFinalResult(self, answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Trapezium Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.tTxt = WrappingLabel(self.mainFrame, text="Top:  ", font=(font, 20))
    self.tTxt.grid(row=0, column=0, padx=2, sticky="e")
    self.tEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.tEntry.grid(row=0, column=1, sticky="w")
    self.bTxt = WrappingLabel(self.mainFrame, text="Bottom:  ", font=(font, 20))
    self.bTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.bEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.bEntry.grid(row=1, column=1, sticky="w")
    self.hTxt = WrappingLabel(self.mainFrame, text="Height:  ", font=(font, 20))
    self.hTxt.grid(row=2, column=0, padx=2, sticky="e")
    self.hEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.hEntry.grid(row=2, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=3, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")

def Rectangle(self):
    def getInputs(self):
        try:
            self.resultTxt.forget_grid()
            self.resultTxt.grid.forget()
        except: pass
        answer = "Ensure that both values, i.e. Breadth/Width and Length, or Length, are/is numerical"
        length = str(self.lengthEntry.get())
        breadth = str(self.breadthEntry.get())
        print(re.search("^\d+\.{0,1}\d{0,1}$", length))
        if re.search("^\d+\.{0,1}\d{0,1}$", length) and re.search("^\d+\.{0,1}\d{0,1}$", breadth):
            if self.typebox.get() == "Rectangle":
                answer = float(length)*float(breadth)
        elif re.search("^\d+\.{0,1}\d{0,1}$", length):
            if self.typebox.get() == "Square":
                answer = float(length)**2
        setFinalResult(self, answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Rectangle/Square Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")

    self.breadthTxt = WrappingLabel(self.mainFrame, text="Breadth/Width:  ", font=(font, 20))
    self.breadthTxt.grid(row=2, column=0, padx=2, sticky="e")
    self.breadthEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.breadthEntry.grid(row=2, column=1, sticky="w")
    self.lengthTxt = WrappingLabel(self.mainFrame, text="Length:  ", font=(font, 20))
    self.lengthTxt.grid(row=1, column=0, padx=2, sticky="e")
    self.lengthEntry = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.lengthEntry.grid(row=1, column=1, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=3, column=1, pady=10, padx=2, sticky="w")

    def changeTypebox(self):
        print("heheh")
        print(self.typebox.get())
        if self.typebox.get() == "Square":
            self.breadthTxt.forget()
            self.breadthEntry.forget()
        else:
            self.breadthTxt.grid(row=2, column=0, padx=2, sticky="e")
            self.breadthEntry.grid(row=2, column=1, sticky="w")

    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font, 20))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Rectangle", "Square"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types, postcommand=lambda:changeTypebox(self))
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=4,column=1,padx=2,columnspan=4, sticky="w")

def Circle(self):
    def getInputs(self):
        try:
            self.resultTxt.forget_grid()
            self.resultTxt.grid.forget()
        except: pass
        answer = "Ensure that values, i.e. Either Circumference Or Radius, are valid"
        r = str(self.ce.get())
        c = str(self.re.get())
        a = str(self.angle.get())
        if ((True if str(type(re.search("^\d+\.{0,1}\d{0,1}$", r))) != "<class 'NoneType'>" else False) ^ (True if str(type(re.search("^\d+\.{0,1}\d{0,1}$", c))) != "<class 'NoneType'>" else False)) or (type(re.search("^\d+\.{0,1}\d{0,1}$", r)) and type(re.search("^\d+\.{0,1}\d{0,1}$", a))):
            print("yes")
            if re.search("^\d+\.{0,1}\d{0,1}$", r):
                print("uwu")
                answer = circle(r)
            elif re.search("^\d+\.{0,1}\d{0,1}$", c):
                print("hmm")
                answer = circle(float(c)/math.pi/float(2))
                if self.typebox.get() == "Semicircle":
                    answer = float(answer)/float(2)
            elif self.typebox.get() == "Sector":
                if re.search("^\d+\.{0,1}\d{0,1}$", a) and re.search("^\d+\.{0,1}\d{0,1}$", r):
                    if float(a) >= 0.0 and float(a) <= 360.0:
                        answer = sector(r, a)
        setFinalResult(self, answer)
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Circle/Semicircle Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.ct = WrappingLabel(self.mainFrame, text="Circumference:  ", font=(font, 20))
    self.ct.grid(row=1, column=0, padx=2, sticky="e")
    self.ce = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.ce.grid(row=1, column=1, padx=2, sticky="w")
    self.rt = WrappingLabel(self.mainFrame, text="Radius:  ", font=(font, 20))
    self.rt.grid(row=2, column=0, padx=2, sticky="e")
    self.re = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.re.grid(row=2, column=1, padx=2, sticky="w")
    self.at = WrappingLabel(self.mainFrame, text="Angle:  ", font=(font, 20))
    self.at.grid(row=3, column=0, padx=2, sticky="e")
    self.angle = ttk.Entry(self.mainFrame, width=20, font=(font, 12))
    self.angle.grid(row=3, column=1, padx=2, sticky="w")
    self.typetext = WrappingLabel(self.mainFrame, text="Type:  ", font=(font, 20))
    self.typetext.grid(row=0, column=0, padx=2, sticky="e")
    self.types = ["Circle", "Semicircle", "Sector"]
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=self.types)
    self.typebox.current(0)
    self.typebox.grid(row=0, column=1, padx=2, sticky="w")
    self.sendData = ttk.Button(self.mainFrame, text="Calculate", style='Accent.TButton', command=lambda:getInputs(self))
    self.sendData.grid(row=4, column=1, pady=10, padx=2, sticky="w")

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=5,column=1,padx=2,columnspan=4, sticky="w")


def IonicEqn(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = ionicEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Ionic Equation Solver", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Generate", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
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

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Salt Solubilities", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter a Compound and the program will return an output if it is Soluble or Insoluble in water.", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "NaCl")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Check", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

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
            print(final)
            codeReturned = str(calculator().sol(final)[0].num) # Could return error/final value
        except:
            codeReturned="error"
        # else:
        #     codeReturned = "Invalid Input"
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Enter a mathematical expression. currently, only +,-,*,/,(),^ are supported", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "9 + 10")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        try:
            self.resultTxt.packforget()
        except:
            pass
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)

def SolveQuad(self):
    # Input Data
    def getInputs(self):
        eqn = self.inputField.get()
        codeReturned = solveQuad(eqn) # Could return error/final value
        setFinalResult(self, codeReturned)

    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Solving Quadratic Equation", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter an Equation in the format ax^2+bx+c.", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=0, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "x^2+2x+8")
    self.inputField.grid(row=0, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Check", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=1, column=0,pady=10, padx=2)

    def setFinalResult(self, result):

        if len(result[0]) == 1:
            self.resultTxt1 = ttk.Label(self.mainFrame, text="Roots:  {}".format(result[0][0]), font=(font, 20))
            self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        else:
            self.resultTxt1 = ttk.Label(self.mainFrame, text="Roots:  {}, {}".format(result[0][0], result[0][1]), font=(font, 20))
            self.resultTxt1.grid(row=3, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        self.resultTxt2 = ttk.Label(self.mainFrame, text="Completed the Square:  {}".format(result[1]), font=(font, 20))
        self.resultTxt2.grid(row=4, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        self.resultTxt3 = ttk.Label(self.mainFrame, text="Turning Points:  {}, {}".format(str(result[2].split(", ")[0]), result[2].split(", ")[1]), font=(font, 20))
        self.resultTxt3.grid(row=5, columnspan = 2, sticky = tk.W+tk.E, padx=2)
        self.resultTxt4 = ttk.Label(self.mainFrame, text="Y Intercept:  {}".format(result[3]), font=(font, 20))
        self.resultTxt4.grid(row=6, columnspan = 2, sticky = tk.W+tk.E, padx=2)
table=[]
def simsolver(self,column=3):

    print(column)
    row=column-1

    # self.newFrame.pack(side="top", padx=25, pady=18, anchor="nw")
    self.thingFrame = self.addframe()
    self.mainLabel = WrappingLabel(self.thingFrame, text="Simultaneous Equations Solver", font=(font,50,'bold'))
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
        print(row,column)
        table=[]
        for i in range(row):
            table.append([])
            for j in range(column):
                temp=ttk.Entry(self.mainFrame, width=10, font=(font, 12))
                if j<column-2:
                    tempt=str(string.ascii_lowercase[j])+" + "
                elif j==column-2:
                    tempt=str(string.ascii_lowercase[j])+" = "
                else:
                    tempt=""
                self.alpha = ttk.Label(self.mainFrame, text=tempt, font=(font, 20))
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
                    print(calculator().sol(col.get())[0].num)
                    print(calculator().sol(col.get())[0])
                    ret[-1].append(calculator().sol(col.get())[0].num)
                except Exception as e:
                    print(e)
                    print(calculator().sol(col.get()))
                    can=False
        print(ret)
        if can:
            try:
                answer=np.array(solve_sim(*ret))
                print(answer)
                ans=""
                j=0
                for i in answer:
                    ans+=string.ascii_lowercase[j]+" = "+str(i[0][0])+"\n"
                    j+=1
                print(ans)
                self.resultTxt1 = ttk.Label(self.mainFrame, text="Roots:  \n{}".format(ans), font=(font, 20))
                self.resultTxt1.grid(row=row+4,
                columnspan = 2,
                sticky = tk.W+tk.E,
                padx=2)
            except:
                self.resultTxt1 = ttk.Label(self.mainFrame, text="Please enter a valid input.", font=(font, 20))
                self.resultTxt1.grid(row=row+4,
                columnspan = 2,
                sticky = tk.W+tk.E,
                padx=2)
        else:
            self.resultTxt1 = ttk.Label(self.mainFrame, text="Please enter a valid input.", font=(font, 20))
            self.resultTxt1.grid(row=row+4,
             columnspan = 2,
             sticky = tk.W+tk.E,
             padx=2)

    def rese(self,col):
        print(col)
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

def triangle(self):
    self.thingFrame = self.addframe()
    self.mainLabel = WrappingLabel(self.thingFrame, text="Triangle Area Solver", font=(font,50,'bold'))
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter enough angles, or sides to solve for area", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.mainFrame.pack(side="top", padx=25, pady=18, anchor="w")
    anpos=[[4,0],[0,4],[4,4]]
    angles=[]
    for i in anpos:
        temp=ttk.Entry(self.mainFrame, width=10, font=(font, 12))
        temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
        angles.append(temp)
    sidpos=[[2,4],[4,2],[2,2]]
    sides=[]
    for i in sidpos:
        temp=ttk.Entry(self.mainFrame, width=10, font=(font, 12))
        temp.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
        sides.append(temp)
    diagpos=[[3,1],[1,3]]
    for i in diagpos:
        self.resultTxt1 = ttk.Label(self.mainFrame, text="/", font=(font, 20))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
    lines=[[4,1],[4,3]]
    for i in lines:
        self.resultTxt1 = ttk.Label(self.mainFrame, text="-", font=(font, 20))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)

    lines=[[1,4],[3,4]]
    for i in lines:
        self.resultTxt1 = ttk.Label(self.mainFrame, text="|", font=(font, 20))
        self.resultTxt1.grid(row=i[0],column=i[1],padx=2,pady=2, sticky = tk.W+tk.E)
    def onPress():
        try:
            self.resultTxt1.packforget()
        except:
            pass
        ang=[]
        for i in angles:
            if i.get()=="":
                ang.append("?")
            else:
                try:
                    ang.append(math.radians( calculator().sol( i.get())[0].num))
                except Exception as e:
                    print(e)
                    ang.append("?")
        sid=[]
        for i in sides:
            if i.get()=="":
                sid.append("?")
            else:
                try:
                    sid.append(calculator().sol( i.get())[0].num)
                except Exception as e:
                    print(e)
                    sid.append("?")
        answ = areaCalculation.solve_triangle(*sid,*ang)
        if answ != "not possible":
            self.resultTxt1 = ttk.Label(self.mainFrame, text="Area: {} u²".format(answ), font=(font, 20))
            self.resultTxt1.grid(row=6,column=0,padx=2,pady=2, sticky = tk.W+tk.E,columnspan=5)
        else:
            self.resultTxt1 = ttk.Label(self.mainFrame, text="{}".format(answ.title()), font=(font, 20))
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
    self.mainLabel = WrappingLabel(self.thingFrame, text="Equation of Circle", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter the Equation in the following Formats. General Form - (x + a)^2 + (y + b)^2 = r^2, Standard Form - x^2 + y^2 + ax + by + c = 0", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.typeTxt = WrappingLabel(self.mainFrame, text="Type:  ", font=(font, 20))
    self.typeTxt.grid(row=0, column=0, padx=2)
    self.typebox = ttk.Combobox(self.mainFrame, state="readonly", values=["General Form", "Standard Form"], width=50)
    self.typebox.grid(row=0, column=1,padx=2)
    self.inputTxt = WrappingLabel(self.mainFrame, text="Input:  ", font=(font, 20))
    self.inputTxt.grid(row=1, column=0, padx=2)
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "Equation")
    self.inputField.grid(row=1, column=1)
    self.sendData = ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=2, column=0,pady=10, padx=2)

    def setFinalResult(self, result):
        self.resultTxt = ttk.Label(self.mainFrame, text="Result:  {}".format(result), font=(font, 20))
        self.resultTxt.grid(row=3, columnspan = 2, sticky = tk.W+tk.N, padx=2)

def periodicTable(self):
    def getInputs(self):
        self.resFrame.destroy()
        self.resFrame = self.addframe(self.mainFrame)
        e = self.inputField.get().replace(" ", "")
        l=pt.search(e)[:5]
        newf=self.addframe(self.resFrame,borderwidth=1)
            
            
        temp=ttk.Label(newf, text="Atomic Number", font=(font, 10))
        temp.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Period"+", "+"Group", font=(font, 10))
        temp.grid(row=1, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Symbol", font=(font, 15, 'bold'))
        temp.grid(row=2, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Element", font=(font, 12))
        temp.grid(row=3, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text=", ".join(["Protons","Neutrons","Electrons"]), font=(font, 10))
        temp.grid(row=4, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Atomic Mass" , font=(font, 10))
        temp.grid(row=5, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Melting Point" , font=(font, 10))
        temp.grid(row=6, column=0, sticky = tk.N+tk.E, padx=2)

        temp=ttk.Label(newf, text="Boiling Point" , font=(font, 10))
        temp.grid(row=7, column=0, sticky = tk.N+tk.E, padx=2)

        newf.grid(row=0, column=0, sticky = tk.N+tk.E, padx=2)

        r=1
        for i in l:
            newf=self.addframe(self.resFrame,borderwidth=1)
            
            
            temp=ttk.Label(newf, text=int(pt.ELEMENTDATA["AtomicNumber"][i]), font=(font, 10))
            temp.grid(row=0, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(int(pt.ELEMENTDATA["Period"][i]))+", "+str(int(pt.ELEMENTDATA["Group"][i])), font=(font, 10))
            temp.grid(row=1, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(pt.ELEMENTDATA["Symbol"][i]), font=(font, 15, 'bold'))
            temp.grid(row=2, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(pt.ELEMENTDATA["Element"][i]), font=(font, 12))
            temp.grid(row=3, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=", ".join([str(int(pt.ELEMENTDATA[j][i])) for j in ["Protons","Neutrons","Electrons"]]), font=(font, 10))
            temp.grid(row=4, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(pt.ELEMENTDATA["AtomicMass"][i]) , font=(font, 10))
            temp.grid(row=5, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(pt.ELEMENTDATA["MeltingPoint"][i]).title() , font=(font, 10))
            temp.grid(row=6, column=0, sticky = tk.N+tk.W, padx=2)

            temp=ttk.Label(newf, text=str(pt.ELEMENTDATA["BoilingPoint"][i]).title() , font=(font, 10))
            temp.grid(row=7, column=0, sticky = tk.N+tk.W, padx=2)

            newf.grid(row=0, column=r, sticky = tk.N, padx=2)
            r+=1
                
        # self.resFrame.grid(row=1, column=len(l)+1, rowspan=10, columnspan=10,pady=10, padx=2)
        self.resFrame.grid(row=1, column=0, rowspan=len(l)+1, columnspan=10,pady=10, padx=2)

    # User Interface
    self.thingFrame = self.addframe()
    self.thingFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.thingFrame, text="Periodic Table", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.thingFrame, text="Please enter a valid symbol, e.g. H, not L", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")

    self.mainFrame = self.addframe()
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.inputField = ttk.Entry(self.mainFrame, width=50, font=(font, 12))
    self.inputField.insert(0, "H")
    self.inputField.grid(row=0, column=0)
    self.sendData = ttk.Button(self.mainFrame, text="Search", style='Accent.TButton', command=lambda: getInputs(self))
    self.sendData.grid(row=0, column=1,pady=10, padx=2, sticky = tk.W)
    self.resFrame = ttk.Frame(self.mainFrame)
    self.resFrame.grid(row=1, column=0, rowspan=10, columnspan=10,pady=10, padx=2)