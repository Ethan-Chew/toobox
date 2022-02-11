# Created by Ethan
from chemlib import Compound

def saltSolubilities(compound):
    try:
        cmpd = compound
        validate = Compound(compound)
        temp = validate.occurences
        temp = list(temp.keys())
        for val in temp:
            cmpd = cmpd.replace(val, "")
        if len(cmpd) > 0:
            return "Not a Valid Compound. Please check your input."
    except:
        return "Not a Valid Compound. Please check your input."
    
    # Check for SPAN Salts
    if "Na" in compound or "K" in compound or "NH4" in compound or "NO3" in compound:
        return True
    # Check for Chloride Salts
    elif "Cl" in compound:
        if compound == "FeCl2" or compound == "AgCl":
            return False
        else:
            return True
    # Check for Sulfate Salts
    elif "SO4" in compound:
        if compound == "PbSO4" or compound == "CaSO4" or compound == "BaSO4":
            return False
        else:
            return True
    # Check for Carbonate Salts
    elif "CO3" in compound:
        if compound == "Na2CO3" or compound == "K2CO3" or compound == "(NH4)2CO3":
            return True
        else:
            return False
    # Check for Hydroxide and Oxide Salts
    elif "OH" in compound:
        if compound == "NaOH" or compound == "KOH" or compound == "NH4OH" or compound == "Ca2OH" or compound == "Na2O" or compound == "K2O" or compound == "(NH4)2O" or compound == "CaO":
            return True
        else:
            return False
    else:
        return False