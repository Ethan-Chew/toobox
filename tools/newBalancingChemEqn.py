import fractions
from ntpath import join
from chemlib import Element
from chemlib import Compound
import numpy as np
import time
from math import gcd
from functools import reduce

# Example: HCl(aq) + Na(s) -> NaCl(aq) + H2(g)
def balanceChemEqn(equation):
    # Variables
    reactantsCompounds = []
    productsCompounds = []
    uniqueElements = []
    productsOccurances, reactantsOccurances = [], []
    oldProductOccurances, oldReactantOccurances = [], []
    startTime = time.perf_counter()
        
    # Functions
    ## Get Occurances of Elements
    def getOccurances(reactantsCompounds, productsCompounds):
        productsOccurances, reactantsOccurances = [], []
        uniqueElements = []
        
        # Get Reactants
        for i in range(len(reactantsCompounds)):
            splittedCompound = ""
            try:
                if "aq" in reactantsCompounds[i]:
                    try: splittedCompound = reactantsCompounds[i].split("(a")
                    except: pass
                elif "s" in reactantsCompounds[i]:
                    try: splittedCompound = reactantsCompounds[i].split("(s")
                    except: pass
                elif "l" in reactantsCompounds[i]:
                    try: splittedCompound = reactantsCompounds[i].split("(l")
                    except: pass
                elif "g" in reactantsCompounds[i]:
                    try: splittedCompound = reactantsCompounds[i].split("(g")
                    except: pass
            except Exception as err:
                return "Unknown Cmpt", ""
            
            compound = splittedCompound[0]
            cmpdOccurances = Compound(compound).occurences
            for i in range(len(cmpdOccurances)): # Add all elements to uniqueElements
                if list(cmpdOccurances.keys())[i] not in uniqueElements:
                    uniqueElements.append(list(cmpdOccurances.keys())[i])
            reactantsOccurances.append(cmpdOccurances)
            
        # Get Products
        for i in range(len(productsCompounds)):
            splittedCompound = ""
            try:
                if "aq)" in productsCompounds[i]:
                    try: splittedCompound = productsCompounds[i].split("(a")
                    except: pass
                elif "s)" in productsCompounds[i]:
                    try: splittedCompound = productsCompounds[i].split("(s")
                    except: pass
                elif "l)" in productsCompounds[i]:
                    try: splittedCompound = productsCompounds[i].split("(l")
                    except: pass
                elif "g)" in productsCompounds[i]:
                    try: splittedCompound = productsCompounds[i].split("(g")
                    except: pass
            except Exception as err:
                return "Unknown Cmpt", ""
            
            productsOccurances.append(Compound(splittedCompound[0]).occurences)
            
        return productsOccurances, reactantsOccurances, uniqueElements
    
    # Main Code
    ## Data Validation
    try:
        reactantsCompounds, productsCompounds = equation.split(" -> ")
        reactantsCompounds = reactantsCompounds.split(" + ")
        productsCompounds = productsCompounds.split(" + ")
    except:
        return "An Error Occured while Parsing the Equation, please check your formatting."
    else:
        reactantsCompounds, productsCompounds = equation.split(" -> ")
        reactantsCompounds = reactantsCompounds.split(" + ")
        productsCompounds = productsCompounds.split(" + ")
    
    ## Get occurances of Compounds
    try:
        productsOccurances, reactantsOccurances, uniqueElements = getOccurances(reactantsCompounds, productsCompounds)
    except Exception as err:
        print(err)
        return "Occurance Error"
    else:
        productsOccurances, reactantsOccurances, uniqueElements = getOccurances(reactantsCompounds, productsCompounds)
    oldProductOccurances, oldReactantOccurances = productsOccurances, reactantsOccurances
    
    ## Set Elements that are not present as 0
    for i in range(len(productsOccurances)):
        for j in range(len(uniqueElements)):
            if uniqueElements[j] not in productsOccurances[i]:
                productsOccurances[i][uniqueElements[j]] = 0
                
    for i in range(len(reactantsOccurances)):
        for j in range(len(uniqueElements)):
            if uniqueElements[j] not in reactantsOccurances[i]:
                reactantsOccurances[i][uniqueElements[j]] = 0
    
    ## Get LCM of each element
    for elementIndex in range(len(uniqueElements)): # Loop for every element
        elementOccReactant, elementOccProduct = [], []
        lcm, largest, joined = 1, 0, []
        
        # Get the occurances of every element
        for i in range(len(reactantsOccurances)):
            elementOccReactant.append(int(reactantsOccurances[i][uniqueElements[elementIndex]]))
        for i in range(len(productsOccurances)):
            elementOccProduct.append(int(productsOccurances[i][uniqueElements[elementIndex]]))
        
        # Convert to ratio
        if max(elementOccProduct) > max(elementOccReactant):
            largest = max(elementOccProduct)
        else:
            largest = max(elementOccReactant)
        for i in range(len(elementOccReactant)):
            elementOccReactant[i] = elementOccReactant[i]/largest
        for i in range(len(elementOccProduct)):
            elementOccProduct[i] = elementOccProduct[i]/largest
        
        # Find the Minimum value to multiply each element by (Remove floats in ratio)
        joined = elementOccProduct + elementOccReactant
        min = 9999999999999
        for i in range(len(joined)):
            if joined[i] != 0 and joined[i] < min:
                min = joined[i]
        for i in range(len(joined)):
            joined[i] = joined[i]/min
        # joined -- New Ratio of Elements
        elementOccProduct, elementOccReactant = joined[:len(elementOccProduct)-1], joined[len(elementOccProduct)-1:] # Splitting the new ratio back into Product and Reactants

        # Multipling every value in Compound
        for i in range(len(elementOccProduct)):
            if elementOccProduct[i] != 0.0:
                for j in range(len(productsOccurances[i])-1):
                    productsOccurances[i][uniqueElements[j]] = productsOccurances[i][uniqueElements[j]]*round(elementOccProduct[i])
        for i in range(len(elementOccReactant)-1):
            if elementOccReactant[i] != 0.0:
                for j in range(len(reactantsOccurances[i])):
                    reactantsOccurances[i][uniqueElements[j]] = reactantsOccurances[i][uniqueElements[j]]*round(elementOccReactant[i])
    print(productsOccurances, reactantsOccurances)

print(balanceChemEqn("Ba(OH)2(aq) + NH4Cl(aq) -> BaCl2(s) + NH3(g) + H2O(l)"))