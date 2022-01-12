# Created by Ethan Chew
from chemlib import Element
from chemlib import Compound
import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk
# Example: 2HCl(aq) + 2Na(s) -> 2NaCl(aq) + H2(g)

class ionicEqn(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)
        self.setup_widgets()
    
    def setup_widgets(self):
        ## Ionic Eqn Screen Frame
        self.ionicEqnScreen = ttk.Frame(self.paned, padding=5)
        self.notebook = ttk.Notebook(self.ionicEqnScreen, padding=3)
        self.notebook.pack(fill="both", expand=True)

        ## Sizegrip
        self.sizegrip = ttk.Sizegrip(self)
        self.sizegrip.pack(side="right")

        ## Top Labels
        self.welcomeFrame = ttk.Frame(self.notebook)
        self.welcomeFrame.pack(side="top", padx=25, pady=18, anchor="w")
        self.helloUserLab = ttk.Label(self.welcomeFrame ,text="Hello, TEST", font=("",50, 'bold'))
        self.helloUserLab.pack(pady=2)
        self.welcomeLab = ttk.Label(self.welcomeFrame, text="Welcome to Toobox!",font=("", 15))
        self.welcomeLab.pack(side="left")
        
    def mainCode():
        chemEqn = input("Input: ")

        # Variables
        leftSideElements = {}
        rightSideElements = {}

        # Main
        splittedEqn = chemEqn.split("->")
        leftSideEqn = splittedEqn[0].split(" ")
        rightSideEqn = splittedEqn[1].split(" ")

        def findCharge(element):
            elementValenceElec = int(Element(str(element)).properties["Valence"])
            elementCharge = ""
            if elementValenceElec < 4:
                if elementValenceElec == 1:
                    elementCharge = "+"
                else:
                    elementCharge = "{}-".format(elementValenceElec)
            elif elementValenceElec == 4:
                elementCharge = "4+"
            else:
                elementCharge = "{}-".format(elementValenceElec - 4)
            newElement = ""
            if multiplier.isnumeric():
                newElement = "{}{}{}".format(multiplier,element,elementCharge)
            else:
                newElement = "{}{}".format(element,elementCharge)
            return newElement

        ## Split if aqueous

        for item in leftSideEqn:
            if item != "" and item != "+":
                splittedItem = item.split("(")
                if splittedItem[1] == "aq)":
                    multiplier = splittedItem[0][0]
                    compoundOccurances = Compound(splittedItem[0]).occurences
                    if len(compoundOccurances) != 1:
                        counter = len(leftSideElements)
                        for element in compoundOccurances:
                            newElement = findCharge(element)
                            counter += 1
                            leftSideElements["aq ({})".format(counter)] = newElement
                            
                else:
                    itemKey = "{} ({})".format(splittedItem[1].replace(")", ""),len(leftSideElements) + 1)
                    leftSideElements[itemKey] = splittedItem[0]

        for item in rightSideEqn:
            if item != "" and item != "+":
                splittedItem = item.split("(")
                if splittedItem[1] == "aq)":
                    multiplier = splittedItem[0][0]
                    compoundOccurances = Compound(splittedItem[0]).occurences
                    if len(compoundOccurances) != 1:
                        counter = len(rightSideElements)
                        for element in compoundOccurances:
                            newElement = findCharge(element)
                            counter += 1
                            rightSideElements["aq ({})".format(counter)] = newElement
                else:
                    itemKey = "{} ({})".format(splittedItem[1].replace(")", ""),len(leftSideElements) + 1)
                    rightSideElements[itemKey] = splittedItem[0]

        ## Remove Spectator Ions
        leftData = list(leftSideElements.keys())
        leftElements = list(leftSideElements.values())
        rightData = list(rightSideElements.keys())
        rightElements = list(rightSideElements.values())

        for l in range(len(leftSideElements)):
            for r in range(len(rightSideElements)):
                if leftElements[l] == rightElements[r]:
                    if "aq" in leftData[l] and "aq" in rightData[r]:
                        leftSideElements.pop(leftData[l])
                        rightSideElements.pop(rightData[r])

        ## Return final ionic
        finalIonic = ""
        leftData = list(leftSideElements.keys())
        leftElements = list(leftSideElements.values())
        rightData = list(rightSideElements.keys())
        rightElements = list(rightSideElements.values())

        for i in range(len(leftElements)):
            finalIonic += leftElements[i]
            finalIonic += "({})".format(leftData[i].split()[0])
            finalIonic += " +"
            finalIonic += " "
        finalIonic = finalIonic[:-2]
        finalIonic += "->"
        for i in range(len(rightElements)):
            finalIonic += " "
            finalIonic += rightElements[i]
            finalIonic += "({})".format(rightData[i].split()[0])
            finalIonic += " +"
        finalIonic = finalIonic[:-2]
        print("Output: {}".format(finalIonic))