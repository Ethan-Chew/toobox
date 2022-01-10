a, b, c = 0, 0, 0
while True:
    ## Check if user typed x^2 or x and let that = 1
    eqn = input("Enter Variables for Quadratic Equation (ax^2+bx+c): ")
    a = eqn[0:eqn.find("x^2")]
    if "x+" in eqn:
        b = eqn[eqn.find("x^2") + 3:eqn.find("x+")]
    elif "x-" in eqn:
        b = eqn[eqn.find("x^2") + 3:eqn.find("x-")]
    c = eqn[eqn.find(b) + 1 + len(b):len(eqn)]
    
    try:
        a,b,c = int(a),int(b),int(c)
        break
    except TypeError:
        print("TypeErr")
    except ValueError:
        print("ValErr")

def QuadRoots():
    discriminant = ((b**2)-(4*a*c))
    if discriminant < 0:
        print("No Real Solution")
        return

    discriminant = discriminant**0.5
    if discriminant < 0:
        print("No Real Solution")
        return
    elif discriminant == 0:
        x1=(-b+discriminant)/(2*a)
        print("x = {}".format(x1))
    elif discriminant > 0:
        x1=(-b+discriminant)/(2*a)
        x2=(-b-discriminant)/(2*a)
        print("x1 = {}".format(x1))
        print("x2 = {}".format(x2))
    else:
        print("Err")
    print("y = {}".format(c))

def getCompleteSquare():
    if a > 1:
        b, c = b/a, c/a
        a = 1
        getTurningPoints()
    else:
        getTurningPoints()

def getTurningPoints():
    pass