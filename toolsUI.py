from glob import glob
import string
import tkinter as tk
from tkinter import ttk
import re

from pyparsing import col
from tools.IonicEqn import ionicEqn
from tools.calculator import calculator
from tools.balancingChemEqn import balanceChemEqn
from components.wrappedLabel import WrappingLabel
from tools.saltSolubilities import saltSolubilities
from tools.solveQuad import solveQuad
from tools.areaCalculation import *
from tools.sim_eqn import *
import math
font="TkDefaultFont"
def ChemicalEquation(self):
    # Input Data
    def getInputs(self):
        chemEqn = self.inputField.get()
        codeReturned = balanceChemEqn(chemEqn) # Could return error/final value
        setFinalResult(self, codeReturned)
    
    # User Interface
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Chemical Equation Balancer", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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

def notUsable(self):
    # Top Labels
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.place(anchor="center", relx=0.5, rely=0.5)
    self.wipText = WrappingLabel(self.welcomeFrame, text="This is a Work in Progress", font=(font, 30, 'bold'), justify="center")
    self.wipText.pack(side="top", pady=2)
    self.wipTextA = WrappingLabel(self.welcomeFrame, text="Check back soon!", font=(font, 20), justify="center")
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
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Parallelogram Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Trapezium Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Rectangle/Square Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Circle/Semicircle Area Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Ionic Equation Solver", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter the Chemical Equation like in the following example: 'Compound(State) + Compound2(State) + ... -> Compound3(State) + Compound4(State) + ...'", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Salt Solubilities", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter a Compound and the program will return an output if it is Soluble or Insoluble in water.", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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
        final=""
        for i in inputVal:
            if i!=" ":
                final+=i
        try:
            codeReturned = str(calculator().sol(inputVal))[0] # Could return error/final value
        except:
            codeReturned="error"
        setFinalResult(self, codeReturned)

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Calculator", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Enter a mathematical expression. currently, only +,-,*,/,(),^ are supported", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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

    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainLabel = WrappingLabel(self.welcomeFrame, text="Solving Quadratic Equation", font=(font,50,'bold'))
    self.mainLabel.pack(side="top", pady=2, fill="x", expand="yes")
    self.infoLabel = WrappingLabel(self.welcomeFrame, text="Please enter an Equation in the format ax^2+bx+c.", font=(font, 15))
    self.infoLabel.pack(side="top", pady=2, fill="x", expand="yes")
    
    self.mainFrame = ttk.Frame(self.notebook)
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
def simsolver(self,row=4,column=4):
    print(row,column)
    self.welcomeFrame = ttk.Frame(self.notebook)
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    self.mainFrame = ttk.Frame(self.notebook)
    self.mainFrame.pack(padx=25, pady=18, anchor="w")
    self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
    def gen_table(row,column):
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
                temp.grid(row=i,column=j*2,padx=2,pady=2)
                table[i].append(temp)
        return table
    table=gen_table(row,column)
    def onPress():
        #solve_sim
        ret=[]
        for row in table:
            ret.append([])
            for col in row:
                ret[-1].append(col.get())
        print(ret)
    def rese(self,row,col):
        self.welcomeFrame.pack_forget()
        self.clearScreen()
        simsolver(self,row,col)
    ttk.Button(self.mainFrame, text="Solve", style='Accent.TButton', command=onPress,width=10).grid(row=row+3, column=0,pady=2, padx=2)
    ttk.Button(self.mainFrame, text="Add Variable", style='Accent.TButton', command=(lambda: rese(self,min(row+1,25),min(row+1,25))),width=10).grid(row=row+2, column=0,pady=2, padx=2)
    ttk.Button(self.mainFrame, text="Remove Variable", style='Accent.TButton', command=(lambda: rese(self,max(row-1,3),max(row-1,3))),width=10).grid(row=row+2, column=2,pady=2, padx=2)



