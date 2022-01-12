# Created by Ethan Chew
from re import L
from sys import base_exec_prefix
from tkinter import ttk
from chemlib import Element
from chemlib import Compound
# Example: HCl(aq) + Na(s) -> NaCl(aq) + H2(g)

equation = "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)"
class balanceChemEqn(ttk.Frame):
    def __init__(self, parent):
        self.config_widgets()

    def config_widgets(self):
        pass

    def mainCode(equation):
        # Variables
        reactantsCompounds = []
        productsCompounds = []
        reactantsOccurances = {}
        productsOccurances = {}

        # Main
        reactantsCompounds, productsCompounds = equation.split(" -> ")
        reactantsCompounds = reactantsCompounds.split(" + ")
        productsCompounds = productsCompounds.split(" + ")

        # Function to get occurances
        def getOccurances():
            reactantsOccurances = {}
            productsOccurances = {}

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
                splittedCompound = reactantsCompounds[i].split("(")
                occurences = Compound(splittedCompound[0]).occurences
                occurences.update((x, y*oldMul) for x, y in occurences.items())
                reactantsOccurances = reactantsOccurances | occurences

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
                occurences = Compound(splittedCompound[0]).occurences
                occurences.update((x, y*oldMul) for x, y in occurences.items())
                productsOccurances = productsOccurances | occurences
        
            return reactantsOccurances, productsOccurances

        reactantsOccurances, productsOccurances = getOccurances()

        ## Loop indefinately until both sides are balanced
        while productsOccurances != reactantsOccurances:
            reactantsKeys = list(reactantsOccurances.keys())
            reactantsVals = list(reactantsOccurances.values())
            productsKeys = list(productsOccurances.keys())
            productsVals = list(productsOccurances.values())
            numOfElements = len(productsOccurances)

            if reactantsOccurances == productsOccurances:
                break

            for i in range(numOfElements):
                for j in range(numOfElements):
                    print(reactantsKeys[i], i)
                    print(productsKeys[j], j)
                    if reactantsKeys[i] == productsKeys[j]:
                        if reactantsVals[i] != productsVals[j]:
                            print(reactantsKeys[i], productsKeys[j])
                            print(reactantsVals[i], productsVals[j])
                            # Same element, number of occurances is not the same
                            ## Find the compound relating to the lower number of occurances
                            if reactantsVals[i] > productsVals[j]:
                                # Right side lesser
                                for e in range(len(productsCompounds)):
                                    if productsKeys[j] in productsCompounds[e]:
                                        # Element in Compound
                                        addedMultiplier = reactantsVals[j] - productsVals[i] # How much to increment the number of compounds by
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
                                        addedMultiplier = productsVals[j] - reactantsVals[i] # How much to increment the number of compounds by
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