# Created by Ethan Chew
def solveQuad(eqn):
    a, b, c = 0,0,0
    # Return Values
    roots, completedSq, turningPoint, yIntercept = [], "", "", 0

    def validation(): # Validate User Input
        global a,b,c
        try: # Try to Parse Values of a, b and c
            a = eqn[0:eqn.find("x^2")]
            if "x+" in eqn:
                b = eqn[eqn.find("x^2") + 3:eqn.find("x+")]
            elif "x-" in eqn:
                b = eqn[eqn.find("x^2") + 3:eqn.find("x-")]
            c = eqn[eqn.find(b) + 1 + len(b):len(eqn)]
            if a == "":
                a = +1
        except:
            return "Format Err"

        try: # Format Values if "+" is present (You dont write numbers as +1 + +2)
            a = str(a).replace("+", "")
            b = str(b).replace("+", "")
            c = str(c).replace("+", "")
            a,b,c = int(a),int(b),int(c)
        except:
            return "Val Err"

        return "{} {} {}".format(a, b, c)

    validationOutcome = validation()
    if validationOutcome == "Format Err":
        return "Format Error, please follow stated format."
    elif validationOutcome == "Val Err":
        return "a/b/c is not a number, please ensure that it is one."
    else:
        a, b, c = validationOutcome.split(" ")
        a,b,c = int(a),int(b),int(c)

    # Find x and y intercepts
    discriminant = ((b**2)-(4*a*c)) # Discriminant Formula (b^2 - 4ac)
    if discriminant < 0:
        roots.append("No Real Solution")
    else:
        discriminant = discriminant**0.5 # Square Root of Discriminant
        if discriminant < 0:
            roots.append("No Real Solution")
        elif discriminant == 0:
            x1=(-b+discriminant)/(2*a)
            roots.append(x1)
        elif discriminant > 0:
            x1=(-b+discriminant)/(2*a)
            x2=(-b-discriminant)/(2*a)
            roots.append(x1, x2)
    yIntercept = c
    
    # Use Completing the Square method
    tempVal = (b/2)**2
    newX = (-b+(b**2-(4*a*tempVal)))/(2*a)
    holdX = newX
    if (newX > 0):
        splittedX = list(str(newX))
        splittedX.insert(0, "-")
        newX = "".join(splittedX)
    else:
        newX = abs(newX)
        if (newX > 0):
            splittedX = list(str(newX))
            splittedX.insert(0, "+")
            newX = "".join(splittedX)
    newC = c-tempVal
    if (newC > 0):
        splittedC = list(str(newC))
        splittedC.insert(0, "+")
        newC = "".join(splittedC)
    completedSq = "(x{})^2{}".format(newX, str(newC))
    turningPoint = "{}, {}".format(str(holdX), str(newC))

    return roots, completedSq, turningPoint, yIntercept