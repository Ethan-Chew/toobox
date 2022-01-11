# Created by Ethan Chew
from re import L
from sys import base_exec_prefix
from chemlib import Element
from chemlib import Compound
# Example: HCl(aq) + Na(s) -> NaCl(aq) + H2(g)

equation = "HCl(aq) + Na(s) -> NaCl(aq) + H2(g)"

# Variables
leftSideCompounds = []
rightSideCompounds = []
leftSideOccurances = {}
rightSideOccurances = {}

# Main
leftSideCompounds, rightSideCompounds = equation.split(" -> ")
leftSideCompounds = leftSideCompounds.split(" + ")
rightSideCompounds = rightSideCompounds.split(" + ")

# Function to get occurances
def getOccurances():
    leftSideOccurances = {}
    rightSideOccurances = {}

    ## Loop through left side components
    for i in range(len(leftSideCompounds)):
        oldMul = ""
        for alpha in range(len(leftSideCompounds[i])):
            if leftSideCompounds[i][alpha].isdigit():
                oldMul += leftSideCompounds[i][alpha]
            else:
                break
        if oldMul == 0 or oldMul == "":
            oldMul = 1
        else:
            oldMul = int(oldMul)
        splittedCompound = leftSideCompounds[i].split("(")
        occurences = Compound(splittedCompound[0]).occurences
        occurences.update((x, y*oldMul) for x, y in occurences.items())
        leftSideOccurances = leftSideOccurances | occurences

    ## Loop through right side components
    for i in range(len(rightSideCompounds)):
        oldMul = ""
        for alpha in range(len(rightSideCompounds[i])):
            if rightSideCompounds[i][alpha].isdigit():
                oldMul += rightSideCompounds[i][alpha]
            else:
                break
        if oldMul == 0 or oldMul == "":
            oldMul = 1
        else:
            oldMul = int(oldMul)
        splittedCompound = rightSideCompounds[i].split("(")
        occurences = Compound(splittedCompound[0]).occurences
        occurences.update((x, y*oldMul) for x, y in occurences.items())
        rightSideOccurances = rightSideOccurances | occurences
 
    return leftSideOccurances, rightSideOccurances

leftSideOccurances, rightSideOccurances = getOccurances()

## Loop indefinately until both sides are balanced
while rightSideOccurances != leftSideOccurances:
    leftSideKeys = list(leftSideOccurances.keys())
    leftSideVals = list(leftSideOccurances.values())
    rightSideKeys = list(rightSideOccurances.keys())
    rightSideVals = list(rightSideOccurances.values())
    numOfElements = len(rightSideOccurances)

    if leftSideOccurances == rightSideOccurances:
        break

    for i in range(numOfElements):
        for j in range(numOfElements):
            if leftSideKeys[i] == rightSideKeys[j]:
                if leftSideVals[i] != rightSideVals[j]:
                    # Same element, number of occurances is not the same
                    ## Find the compound relating to the lower number of occurances
                    if leftSideVals[i] > rightSideVals[j]:
                        # Right side lesser
                        for e in range(len(rightSideCompounds)):
                            if rightSideKeys[j] in rightSideCompounds[e]:
                                # Element in Compound
                                multiplier = leftSideVals[i] - rightSideVals[j]
                                compound = list(rightSideCompounds[e])
                                # Element in Compound
                                addedMultiplier = rightSideVals[j] - leftSideVals[i]
                                oldMul = ""
                                compound = list(leftSideCompounds[e])
                                if compound[0].isdigit(): # Multiplier is present
                                    for alpha in compound:
                                        if alpha.isdigit():
                                            oldMul += str(alpha)
                                            compound.pop(0)
                                        else:
                                            break
                                    oldMul = int(oldMul)
                                    oldMul += addedMultiplier
                                    compound[0] = str(oldMul)
                                else:
                                    compound.insert(0, str(multiplier))
                                rightSideCompounds[e] = "".join(compound)
                                leftSideOccurances, rightSideOccurances = getOccurances()
                    else:
                        # Left side lesser
                        for e in range(len(leftSideCompounds)):
                            if leftSideKeys[i] in leftSideCompounds[e]:
                                # Element in Compound
                                addedMultiplier = rightSideVals[j] - leftSideVals[i]
                                oldMul = ""
                                compound = list(leftSideCompounds[e])
                                if compound[0].isdigit(): # Multiplier is present
                                    for alpha in compound:
                                        if alpha.isdigit():
                                            oldMul += str(alpha)
                                            compound.pop(0)
                                        else:
                                            break
                                    oldMul = int(oldMul)
                                    compound.insert(0, str(oldMul + addedMultiplier))
                                else: # Currently no multiplier
                                    compound.insert(0, str(addedMultiplier + 1))
                                leftSideCompounds[e] = "".join(compound)
                                leftSideOccurances, rightSideOccurances = getOccurances()
                                if leftSideOccurances == rightSideOccurances:
                                    break
    if leftSideOccurances == rightSideOccurances:
        break

print(leftSideCompounds)
print(rightSideCompounds)