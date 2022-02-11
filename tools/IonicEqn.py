# Created by Ethan
from math import prod
from chemlib import Element
from chemlib import Compound
import tkinter as tk
from tkinter import Canvas, PhotoImage, ttk
import re
# Example: 2HCl(aq) + 2Na(s) -> 2NaCl(aq) + H2(g)

def ionicEqn(equation):
    # Variables
    productEqn, reactantEqn = [], []
    ionicProduct, ionicReactant = [], []
    specAnions = ["NH4+", "H3O+", "CH3COO-", "C2H3O2-", "CO32-", "HCO3-", "OH-", "NO3-", "PO43-", "SO42-", "HSO4-", "MnO4-", "Cr2O72-", "SO32-", "ClO3-", "ClO2-", "CrO42-", "CN-", "ClO-", "NO2-", "ClO4-", "SO32-", "S2O32-"]
    specAnionsNC = ["NH4", "H3O", "CH3COO", "C2H3O2", "CO", "HCO3", "OH", "NO3", "PO4", "SO4", "HSO4", "MnO4", "Cr2O7", "SO3", "ClO3", "ClO2", "CrO4", "CN", "ClO", "NO2", "ClO4", "SO3", "S2O3"]

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
    else:
        splittedEqn = equation.split(" -> ")
        reactantEqn = splittedEqn[0].split(" ")
        productEqn = splittedEqn[1].split(" ")

    ## Functions
    ### Find the Charge of an Element
    def findCharge(element):
        elementValenceElec = round(Element(str(element)).properties["Valence"])
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
        return elementCharge
    
    # Format the Compound and Return it
    def formatCompound(compound, cmpdMultiplier):
        anion, mul = "", 0
        formattedCompound = []
        # Check if Compound has 'Special Anions'
        for val in specAnionsNC:
            if val in compound:
                anion = val
                ## Find 'Multiplier' for Anion
                if "(" in compound and ")" in compound:
                    mul = int(compound[compound.find(")")+1:len(compound)])
                else:
                    mul = 1
                ## Remove from formattedCmpd
                if mul == 1:
                    compound = compound.replace("{}".format(anion), "")
                else:
                    compound = compound.replace("({}){}".format(anion, str(mul)), "")
                ## Get Charge
                for chargedAnion in specAnions:
                    if anion in chargedAnion:
                        anion = chargedAnion
                        break
                ## Add Multiplier
                if mul != 1:
                    anion = "{}{} {}".format(str(cmpdMultiplier*mul), anion, "(aq)")
                else:
                    if cmpdMultiplier != 1:
                        anion = "{}{} {}".format(str(cmpdMultiplier), anion, "(aq)")
                    else:
                        anion = "{} {}".format(anion, "(aq)")
                ## Add to Formatted Cmpd Array
                formattedCompound.append(anion)
                break
        # Get Occurances of Remaining Elements
        elementOccurances = Compound(compound).occurences
        remainElements, remainMul = list(elementOccurances.keys()), list(elementOccurances.values())
        for i in range(len(remainElements)):
            elementCharge = findCharge(remainElements[i])
            if remainMul[i] == 1:
                if cmpdMultiplier != 1:
                    formattedCompound.append("{}{}{} (aq)".format(cmpdMultiplier,remainElements[i], elementCharge))
                else:
                    formattedCompound.append("{}{} (aq)".format(remainElements[i], elementCharge))
            else:
                formattedCompound.append("{}{}{} (aq)".format(cmpdMultiplier*remainMul[i],remainElements[i], elementCharge))
        
        return formattedCompound
    
    
    try:
        # Loop through both left and right sides
        for rawCompound in reactantEqn:
            # Check if Compound is Aqueous (State Symbols)
            if "(aq)" in rawCompound:
                reactantEqn.remove(rawCompound)
                compound = rawCompound.replace("(aq)", "")
                cmpdMul = ""
                try: 
                    if compound[0].isnumeric():
                        cmpdMul = int(re.findall('[0-9]+', compound)[0])
                    else: cmpdMul = 1
                except: cmpdMul = 1
                ionicReactant = formatCompound(compound, cmpdMul) + ionicReactant
        for rawCompound in productEqn:
            # Check if Compound is Aqueous (State Symbols)
            if "(aq)" in rawCompound:
                productEqn.remove(rawCompound)
                compound = rawCompound.replace("(aq)", "")
                cmpdMul = ""
                try: 
                    if compound[0].isnumeric():
                        cmpdMul = int(re.findall('[0-9]+', compound)[0])
                    else: cmpdMul = 1
                except: cmpdMul = 1
                ionicProduct = formatCompound(compound, cmpdMul) + ionicProduct
        
        # Remove Spectator Ions
        for reactant in ionicReactant:
            for product in ionicProduct:
                if reactant == product:
                    ionicProduct.remove(product)
                    ionicReactant.remove(reactant)
        
        # Combine the Equation
        ionicEquation = ""
        for reactant in ionicReactant:
            ionicEquation += reactant
            ionicEquation += " + "
        for reactant in reactantEqn:
            if reactant != "+":
                ionicEquation += reactant
                ionicEquation += " + "
        ionicEquation = ionicEquation[:len(ionicEquation)-3]
        ionicEquation += " -> "
        for product in ionicProduct:
            ionicEquation += product
            ionicEquation += " + "
        for product in productEqn:
            if product != "+":
                ionicEquation += product
                ionicEquation += " + "
        ionicEquation = ionicEquation[:len(ionicEquation)-3]
        return ionicEquation
    except:
        return "Unknown Error. Please try again."