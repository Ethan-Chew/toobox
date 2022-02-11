# Ethan
# Some Granwyn
def solveQuad(eqn):
    a, b, c = 0,0,0
    # Return Values
    shape, roots, completedSq, turningPoint, yIntercept = "", [], "", "", 0

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
    shape = "Concave Downwards ∩" if a < 0 else ("Concave Upwards U" if a > 0 else "Linear")
    discriminant = ((b**2)-(4*a*c)) # Discriminant Formula (b^2 - 4ac)
    if discriminant < 0:
        roots.append("No Real Solution")
    else:
        discriminant = discriminant**0.5 # Square Root of Discriminant
        if discriminant < 0:
            roots.append("No Real Solution")
        elif discriminant == 0:
            x1=(-b-discriminant)/(2*a)
            roots.append(x1)
        elif discriminant > 0:
            x1=(-b+discriminant)/(2*a)
            x2=(-b-discriminant)/(2*a)
            roots.append(x1, x2)
    yIntercept = c
    
    # Use Completing the Square method
    x,y = 0, 0
    if b**2 - 4*a*c > 0:
        x = ((-b+((b**2-4*a*c)**0.5))/(2*a)+(-b-((b**2-4*a*c)**0.5))/(2*a))/2
        y = float(a*x**2 + b*x + c)
        turningPoint = "{}, {}".format(x, y)
    if b**2 - 4*a*c < 0:
        x = -(b/(2*a))
        y = -(a*(b/(2*a))**2) + c
        turningPoint = "{}, {}".format(x, y)
    if b**2 - 4*a*c == 0:
        x = (-b+((b**2-4*a*c)**0.5))/(2*a)
        y = float(a*x**2 + b*x + c)
        turningPoint = "{}, {}".format(x, y)
    if y > 0:
        temp = list(str(y))
        temp.insert(0, "+")
        y = ''.join(temp)
    if x > 0:
        temp = list(str(x))
        temp.insert(0, "-")
        x = ''.join(temp)
    else:
        temp = list(str(x))
        temp.pop(0)
        temp.insert(0, "+")
        x = ''.join(temp)
    completedSq = "(x{})²{}".format(x, y)

    return roots, completedSq, turningPoint, yIntercept, shape

if __name__=="__main__":
    print(solveQuad("x^2+2x+8"))
    print(solveQuad("5x^2+9x+8"))