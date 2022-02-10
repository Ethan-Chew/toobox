# Created by Ethan Chew
from chemlib import Element
from chemlib import Compound
import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk
import re
# Example: 2HCl(aq) + 2Na(s) -> 2NaCl(aq) + H2(g)

def ionicEqn(equation):
    # Variables
    leftSideElements, rightSideElements = {}, {}
    rightSideEqn, leftSideEqn = [], []
    diatomicIonicAnions = ["NH4+", "H3O+", "CH3COO-", "C2H3O2-", "CO32-", "HCO3-", "OH-", "NO3-", "PO43-", "SO42-", "HSO4-"]

    # Main
    ## Data Validation
    def validate():
        try:
            splittedEqn = equation.split("->")
            testLef = splittedEqn[0].split(" ")
            textRig = splittedEqn[1].split(" ")
        except:
            return "Format Err"
        if "aq" not in equation:
            return "No aq"

    validationOutcome = validate()
    if validationOutcome == "Format Err":
        return "Invalid Equation Format, please follow the format stated."
    elif validationOutcome == "No aq":
        return "The Equation does not have an Aqueous Substance. Please check the Equation entered again."

    splittedEqn = equation.split(" -> ")
    leftSideEqn = splittedEqn[0].split(" ")
    rightSideEqn = splittedEqn[1].split(" ")

    def findCharge(element):
        elementValenceElec = int(Element(str(element)).properties["Valence"])
        elementCharge = ""
        if elementValenceElec < 4:
            if elementValenceElec == 1:
                elementCharge = "+"
            else:
                elementCharge = "{}+".format(elementValenceElec)
        elif elementValenceElec == 4:
            elementCharge = "4+"
        else:
            if elementValenceElec - 4 != 1:
                elementCharge = "{}-".format(elementValenceElec - 4)
            else:
                elementCharge = "-"
        newElement = ""
        if multiplier.isnumeric():
            newElement = "{}{}{}".format(multiplier,element,elementCharge)
        else:
            newElement = "{}{}".format(element,elementCharge)
        return newElement

    try:
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
                            numOfAtoms = compoundOccurances[element]
                            if numOfAtoms == 1:
                                numOfAtoms = ""
                            else :
                                numOfAtoms = str(numOfAtoms)
                            newElement = findCharge(element)
                            counter += 1
                            leftSideElements["aq ({})".format(counter)] = '{}{}'.format(numOfAtoms, newElement)
                            
                else:
                    item = splittedItem[1]
                    mul = 0
                    if len(re.findall('[0-9]+', item)) > 0:
                        mul = re.findall(r'[0-9]+', item)
                        for num in mul:
                            item = item.replace(str(num), "")
                            item = item.replace(")", "")
                        mul = int(mul[len(mul)-1])
                    if item.replace(")", "") != "aq":
                        if item.replace(")", "") in diatomicIonicAnions:
                            valIndex = 0
                            for item in diatomicIonicAnions:
                                if item.replace(")", "") in item:
                                    valIndex = diatomicIonicAnions.index(item)
                                    break
                            leftSideElements["aq ({})".replace(len(leftSideElements) + 1)]
                            leftSideElements[itemKey] = diatomicIonicAnions[valIndex]
                    itemKey = "{} ({})".format(item.replace(")", ""),len(leftSideElements) + 1)¿
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
                            numOfAtoms = compoundOccurances[element]
                            if numOfAtoms == 1:
                                numOfAtoms = ""
                            else :
                                numOfAtoms = str(numOfAtoms)
                            newElement = findCharge(element)
                            counter += 1
                            rightSideElements["aq ({})".format(counter)] = '{}{}'.format(numOfAtoms, newElement)
                else:
                    item = splittedItem[1]
                    mul = 0
                    if len(re.findall('[0-9]+', item)) > 0:
                        mul = re.findall(r'[0-9]+', item)
                        for num in mul:
                            item.replace(str(num), "")
                        mul = mul[len(mul)-1]
                    if item.replace(")", "") != "aq":
                        if item.replace(")", "") in diatomicIonicAnions:
                            valIndex = 0
                            for item in diatomicIonicAnions:
                                if item.replace(")", "") in item:
                                    valIndex = diatomicIonicAnions.index(item)
                                    break
                            rightSideElements["aq ({})".replace(len(rightSideElements) + 1)]
                            rightSideElements[itemKey] = diatomicIonicAnions[valIndex]
                    itemKey = "{} ({})".format(item.replace(")", ""),len(rightSideElements) + 1)
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
        if (finalIonic == equation):
            return "Data is already an Ionic Equation/Data is not working"
        else:
            return finalIonic
    except:
        return "Unknown Error. Please try again."
print(ionicEqn("Ba(OH)2(aq) + 2NH4Cl(aq) -> BaCl2(s) + 2H2O(l) + 2NH3(g)"))