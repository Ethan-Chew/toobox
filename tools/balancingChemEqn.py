# Created by Ethan Chew
from re import L
from sys import base_exec_prefix
from tkinter import ttk
from chemlib import Element
from chemlib import Compound
# Example: HCl(aq) + Na(s) -> NaCl(aq) + H2(g)
def balanceChemEqn(equation):
    # Variables
    reactantsCompounds = []
    productsCompounds = []
    reactantsOccurances = {}
    productsOccurances = {}
    
    # Data Validation
    def validateInput():
        reactantsCompounds = []
        productsCompounds = []
        try:
            reactantsCompounds, productsCompounds = equation.split(" -> ")
            reactantsCompounds = reactantsCompounds.split(" + ")
            productsCompounds = productsCompounds.split(" + ")
        except:
            return "Format Err"
        
        try:
            occurancesVal = getOccurances()
            if occurancesVal == "Unknown Cmpt":
                return "Unknown Cmpt"
            elif occurancesVal == "PR Err":
                return "PR Err"
            elif occurancesVal == "Ex Element":
                return "Ex Element"
        except:
            return "Validated"
        
    # Main
    validationOutcome = validateInput()
    if validationOutcome == "Format Err":
        return "Formatting Error, Please follow stated Format."
    elif validationOutcome == "Unknown Cmpt":
        return "Unknown Compound found in Equation."
    elif validationOutcome == "PR Err":
        return "Error while getting Product/Reactant Occurances."
    elif validationOutcome == "Ex Element":
        return "Extra Unknown Element Detected."
    
    reactantsCompounds, productsCompounds = equation.split(" -> ")
    reactantsCompounds = reactantsCompounds.split(" + ")
    productsCompounds = productsCompounds.split(" + ")

    # Function to get occurances
    def getOccurances():
        reactantsOccurances = {}
        productsOccurances = {}

        try:
            ## Loop through left side components
            for i in range(len(reactantsCompounds)):
                oldMul = ""
                for alpha in range(len(reactantsCompounds[i])):
                    if reactantsCompounds[i][alpha].isdigit():
                        oldMul += reactantsCompounds[i][alpha]
                    else:
                        break
                if oldMul == 0 or oldMul == "":
                    oldMul = 1
                else:
                    oldMul = int(oldMul)
                
                if "aq" in reactantsCompounds[i]:
                    splittedCompound = reactantsCompounds[i].split("(a")
                elif "s" in reactantsCompounds[i]:
                    splittedCompound = reactantsCompounds[i].split("(s")
                elif "l" in reactantsCompounds[i]:
                    splittedCompound = reactantsCompounds[i].split("(l")
                elif "g" in reactantsCompounds[i]:
                    splittedCompound = reactantsCompounds[i].split("(g")

                # Find Occurances of Elements
                try:
                    occurences = Compound(splittedCompound[0]).occurences
                except:
                    return "Unknown Cmpt", ""                    
                occurences.update((x, y*oldMul) for x, y in occurences.items())
                reactantsOccurances = reactantsOccurances | occurences
        except:
            return "PR Err", ""

        ## Loop through right side components
        for i in range(len(productsCompounds)):
            oldMul = ""
            for alpha in range(len(productsCompounds[i])):
                if productsCompounds[i][alpha].isdigit():
                    oldMul += productsCompounds[i][alpha]
                else:
                    break
            if oldMul == 0 or oldMul == "":
                oldMul = 1
            else:
                oldMul = int(oldMul)
            splittedCompound = productsCompounds[i].split("(")
            try:
                occurences = Compound(splittedCompound[0]).occurences
            except:
                return "Unknown Cmpt", ""
            occurences.update((x, y*oldMul) for x, y in occurences.items())
            productsOccurances = productsOccurances | occurences

        if len(productsOccurances) != len(reactantsOccurances):
            return "Ex Element", ""

        return reactantsOccurances, productsOccurances

    reactantsOccurances, productsOccurances = getOccurances()
    if reactantsOccurances == "Unknown Cmpt":
        return "Unknown Compound found in Equation."
    elif reactantsOccurances == "PR Err":
        return "Error while getting Product/Reactant Occurances."
    elif reactantsOccurances == "Ex Element":
        return "Extra Unknown Element Detected."

    try:
        ## Loop indefinately until both sides are balanced
        while productsOccurances != reactantsOccurances:
            reactantsKeys = list(reactantsOccurances.keys())
            reactantsVals = list(reactantsOccurances.values())
            productsKeys = list(productsOccurances.keys())
            productsVals = list(productsOccurances.values())
            numOfElements = len(productsOccurances)

            if reactantsOccurances == productsOccurances:
                return equation
            
            for i in range(numOfElements):
                for j in range(numOfElements):
                    if reactantsKeys[i] == productsKeys[j]:
                        if reactantsVals[i] != productsVals[j]:
                            # Same element, number of occurances is not the same
                            ## Find the compound relating to the lower number of occurances
                            if reactantsVals[i] > productsVals[j]:
                                # Right side lesser
                                for e in range(len(productsCompounds)):
                                    if productsKeys[j] in productsCompounds[e]:
                                        # Element in Compound
                                        addedMultiplier = int((reactantsVals[i] - productsVals[j])) # How much to increment the number of compounds by
                                        oldMul = ""
                                        compound = list(productsCompounds[e])
                                        if compound[0].isdigit(): # Multiplier is present
                                            for alpha in compound:
                                                if alpha.isdigit():
                                                    oldMul += str(alpha)
                                                    compound.pop(0)
                                                else:
                                                    break
                                            oldMul = int(oldMul)
                                            compound.insert(0, str(oldMul + addedMultiplier))
                                        else:
                                            compound.insert(0, str(addedMultiplier + 1))
                                        productsCompounds[e] = "".join(compound)
                                        reactantsOccurances, productsOccurances = getOccurances()
                                        reactantsKeys = list(reactantsOccurances.keys())
                                        reactantsVals = list(reactantsOccurances.values())
                                        productsKeys = list(productsOccurances.keys())
                                        productsVals = list(productsOccurances.values())
                                        break
                            else:
                                # Left side lesser
                                for e in range(len(reactantsCompounds)):
                                    if reactantsKeys[i] in reactantsCompounds[e]:
                                        # Element in Compound
                                        addedMultiplier = int((productsVals[j] - reactantsVals[i])) # How much to increment the number of compounds by
                                        oldMul = ""
                                        compound = list(reactantsCompounds[e])
                                        if compound[0].isdigit(): # Multiplier is present
                                            for alpha in compound:
                                                if alpha.isdigit():
                                                    oldMul += str(alpha)
                                                    compound.pop(0)
                                                else:
                                                    break
                                            oldMul = int(oldMul)
                                            compound.insert(0, str(oldMul + addedMultiplier))
                                        else: # Currently no multiplier aka 1 Compound
                                            compound.insert(0, str(addedMultiplier + 1))
                                        reactantsCompounds[e] = "".join(compound)
                                        reactantsOccurances, productsOccurances = getOccurances()
                                        reactantsKeys = list(reactantsOccurances.keys())
                                        reactantsVals = list(reactantsOccurances.values())
                                        productsKeys = list(productsOccurances.keys())
                                        productsVals = list(productsOccurances.values())
                                        break # Break out of Loop once Compound with Element found
            if reactantsOccurances == productsOccurances:
                break

        finalJointReactants = ' + '.join(reactantsCompounds)
        finalJointReactants += ' -> '
        finalJointReactants += ' + '.join(productsCompounds)
        return finalJointReactants
    except:
        return "An Unknown Error has occured."
# print(balanceChemEqn("NH4Cl(aq) + Ba(OH)2(aq) -> BaCl2(aq) + H2O(l) + NH3(g)"))
# print(balanceChemEqn("HCl(aq) + Na(s) -> NaCl(aq) + H2(g)"))