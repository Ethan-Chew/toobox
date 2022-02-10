# Created by Ethan Chew
import random
from chemlib import Element
from chemlib import Compound
# Example: HCl(aq) + Na(s) -> NaCl(aq) + H2(g)
def balanceChemEqn(equation):
    # Variables
    reactantsCompounds = []
    productsCompounds = []
    reactantsOccurances = {}
    productsOccurances = {}
    originalReactants, originalProducts = [], []
    
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
    originalReactants, originalProducts = reactantsCompounds, productsCompounds
    
    def newerparser(compound):
        if "aq" in compound:
            try: splittedCompound = compound.split("(aq)")[0]
            except: pass
        elif "s" in compound:
            try: splittedCompound = compound.split("(s)")[0]
            except: pass
        elif "l" in compound:
            try: splittedCompound = compound.split("(l)")[0]
            except: pass
        elif "g" in compound:
            try: splittedCompound = compound.split("(g)")[0]
            except: pass
        print(splittedCompound)
        return new_parser(splittedCompound)
    def new_parser(compound):
        
        elements={}
        i=0
        while i<=len(compound):
            print(compound[i])
            # print(compound[i])
            if compound[i].isalpha() and compound[i].upper() == compound[i] :
                #start of an element
                ele=compound[i]
                # print(compound[i],compound[i+1].upper(), compound[i+1])
                if compound[i+1].isalpha() and compound[i+1].upper() != compound[i+1]:
                    ele+=compound[i+1]
                    i+=1
                # print(ele)
                print(compound[i+1])
                for j in range(i+1,len(compound)):
                    if compound[j].isnumeric():
                        pass
                    else:
                        break
                # print(j,i)
                if ele in elements:
                    elements[ele]+=int(compound[i+1:j]) if j!= i+1 else 1
                else:
                    elements[ele]=int(compound[i+1:j]) if j!= i+1 else 1
                i=int(j) if j!=i+1 else i
            if compound[i]=="(":
                # print(compound[i:])
                j=int(i)+1
                count=1
                # print(j)
                while j<len(compound):
                    # print(compound[j],count)
                    if compound[j]=="(":
                        count+=1
                    if compound[j]==")":
                        count-=1
                    if count==0:
                        break
                    j+=1
                if j==len(compound):
                    raise Exception("Unbalanced Parentheses")
                else:
                    
                    eles=new_parser(compound[i+1:j])
                    print(eles)
                    for k in range(j+1,len(compound)):
                        if compound[k].isnumeric():
                            pass
                        else:
                            break
                    
                    mul=int(compound[j+1:k]) if k!= j+1 else 1
                    for ele in eles:
                        if ele in elements:
                            elements[ele]+=mul*eles[ele]
                        else:
                            elements[ele]=mul*eles[ele]
                    i=int(k)

                


            i+=1
            return elements
    print(new_parser("OH"))
    exit()
    for i in reactantsCompounds:
        print(newerparser(i))
        exit()

    # Function to get occurances
    def getOccurances():
        reactantsOccurances = {}
        productsOccurances = {}
        splittedCompound=[]
        try:
            ## Loop through left side components
            for i in range(len(reactantsCompounds)):
                oldMul = ""
                print(splittedCompound)
                for alpha in range(len(reactantsCompounds[i])):
                    if reactantsCompounds[i][alpha].isdigit():
                        oldMul += reactantsCompounds[i][alpha]
                    else:
                        break
                if oldMul == 0 or oldMul == "":
                    oldMul = 1
                else:
                    oldMul = int(oldMul)
                
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
                    print(err) 
                    return "Unknown Cmpt", ""
                        
                # Find Occurances of Elements
                try:
                    occurences = Compound(splittedCompound[0]).occurences
                except:
                    return "Unknown Cmpt", ""                    
                occurences.update((x, y*oldMul) for x, y in occurences.items())
                occEle, occOcc = list(occurences.keys()), list(occurences.values())
                if len(reactantsOccurances) == 0:
                    reactantsOccurances = occurences
                else:
                    for i in range(len(occurences)):
                        if occEle[i] not in reactantsOccurances:
                            reactantsOccurances[occEle[i]] = int(occOcc[i])
                        else:
                            reactantsOccurances[occEle[i]] += int(occOcc[i])
                    
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
                
                try:
                    if "aq" in productsCompounds[i]:
                        try: splittedCompound = productsCompounds[i].split("(a")
                        except: pass
                    elif "s" in productsCompounds[i]:
                        try: splittedCompound = productsCompounds[i].split("(s")
                        except: pass
                    elif "l" in productsCompounds[i]:
                        try: splittedCompound = productsCompounds[i].split("(l")
                        except: pass
                    elif "g" in productsCompounds[i]:
                        try: splittedCompound = productsCompounds[i].split("(g")
                        except: pass
                except Exception as err:
                    print(err)  
                    return "Unknown Cmpt", ""
                        
                # Find Occurances of Elements
                try:
                    occurences = Compound(splittedCompound[0]).occurences
                except:
                    return "Unknown Cmpt", ""                    
                occurences.update((x, y*oldMul) for x, y in occurences.items())
                occEle, occOcc = list(occurences.keys()), list(occurences.values())
                if len(productsOccurances) == 0:
                    productsOccurances = occurences
                else:
                    for i in range(len(occurences)):
                        if occEle[i] not in productsOccurances:
                            productsOccurances[occEle[i]] = int(occOcc[i])
                        else:
                            productsOccurances[occEle[i]] += int(occOcc[i])
        except Exception as err:
            print(err)
            return "PR Err", ""

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
            print(reactantsOccurances, productsOccurances)
            for i in range(numOfElements):
                for j in range(numOfElements):
                    if reactantsKeys[i] == productsKeys[j]:
                        if reactantsVals[i] != productsVals[j]:
                            # Same element, number of occurances is not the same
                            ## Find the compound relating to the lower number of occurances
                            if reactantsVals[i] > productsVals[j]:
                                # Right side lesser
                                for e in range(len(productsCompounds)):
                                    if productsKeys[j] in productsCompounds[e]:# why product Compounds? 
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
                                            if oldMul + addedMultiplier > 200:
                                                reactantsCompounds, productsCompounds = random.shuffle(originalReactants), random.shuffle(originalProducts)
                                                break
                                            compound.insert(0, str(oldMul + addedMultiplier))
                                        else:
                                            if addedMultiplier + 1 > 200:
                                                reactantsCompounds, productsCompounds = random.shuffle(originalReactants), random.shuffle(originalProducts)
                                                break
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
                                            if oldMul + addedMultiplier > 200:
                                                reactantsCompounds, productsCompounds = random.shuffle(originalReactants), random.shuffle(originalProducts)
                                                break
                                            compound.insert(0, str(oldMul + addedMultiplier))
                                        else:
                                            if addedMultiplier + 1 > 200:
                                                reactantsCompounds, productsCompounds = random.shuffle(originalReactants), random.shuffle(originalProducts)
                                                break
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
if __name__=="__main__":
    print(balanceChemEqn("Ba(OH)2(aq) + NH4Cl(aq) -> BaCl2(s) + NH3(g) + H2O(l)"))
