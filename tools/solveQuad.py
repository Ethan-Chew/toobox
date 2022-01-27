# Created by Ethan Chew
def solveQuad(eqn):
    a, b, c = 0,0,0
    # Return Values
    roots, completedSq, turningPoint, yIntercept = [], "", "", 0

    def validation():
        global a,b,c
        try:
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
        print(a,b,c)
        try:
            a,b,c = int(a),int(b),int(c)
        except:
            return "Val Err"
    
    validationOutcome = validation()
    if validationOutcome == "Format Err":
        return "Format Error, please follow stated format."
    elif validationOutcome == "Val Err":
        return "a/b/c is not a number, please ensure that it is one."

    # Find x and y intercepts
    try:
        discriminant = ((b**2)-(4*a*c))
        if discriminant < 0:
            roots.append("No Real Solution")
            return

        discriminant = discriminant**0.5
        if discriminant < 0:
            roots.append("No Real Solution")
            return
        elif discriminant == 0:
            x1=(-b+discriminant)/(2*a)
            roots.append(x1)
            return
        elif discriminant > 0:
            x1=(-b+discriminant)/(2*a)
            x2=(-b-discriminant)/(2*a)
            roots.append(x1, x2)
        yIntercept = c
    except:
        return "An Unknown Error has occured while finding the Quadratic Roots of the Equation"
    
    # Use Completing the Square method
    interVal = (b/2)**2
    newX = (-b+((b**2)-(4*a*interVal)))/(2*a)
    completedEqn = "(x{})^2{}".format(newX, c+newX)
    print(completedEqn)

print(solveQuad("x^2+2x+8"))