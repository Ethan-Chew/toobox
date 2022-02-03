import math
from posixpath import split
class circle_equation():
    def mainCode(self, type, eqn):
        if type == "Standard Form":
            # Format: x^2 + y^2 + ax + by + c = 0
            splittedEqn = eqn.split(" ")
            try:
                a = splittedEqn[4]
                b = splittedEqn[6]
                c = splittedEqn[8]

                if "+" in a:
                    a = a.replace("+", "")
                elif "+" in b:
                    b = b.replace("+", "")
                elif "+" in c:
                    c = c.replace("+", "")
                a, b, c = int(a), int(b), int(c)
                ceqn = circle_equation()
                return(ceqn.to_standard_form(a, b, c))
            except: return "Unknown Error"
        else:
            # Format: (x + a)^2 + (y + b)^2 = r^2
            splittedEqn = eqn.split(" ")
            try:
                a = splittedEqn[0].split(" ")
                b = splittedEqn[2].split(" ")
                r = splittedEqn[4]

                a = a[2]
                b = b[2]

                a, b, r= int(a.replace(")^2", "")), int(b.replace(")^2", "")), int(r.replace("^2", ""))
                ceqn = circle_equation()
                return(ceqn.to_general_form(a,b,r))
            except: return "Unknown Error"

    def validate(self,*args):
        try:
            for i in args:
                float(i)
            return True
        except:
            return False
    def to_standard_form(self, a, b, c):
        if not self.validate(a,b,c):
            return "Error"
        
        f=(lambda A:"+ "+str(A) if A>0 else "- "+str(A)[1:])
        A=float(a)/2
        B=float(b)/2
        r=math.sqrt(A**2+B**2-float(c))
        return "(x {})^2 + (y {}) = {}^2".format(f(A),f(B),r)
    def to_general_form(self, a, b, r):
        if not self.validate(a,b,r):
            return "Error"
        f=(lambda A:"+ "+str(A) if A>0 else "- "+str(A)[1:])
        r=math.sqrt(float(r))
        return "x^2 + y^2 {}x {}y {} = 0".format(f(float(a)*2),f(float(b)*2),f(float(a)**2+float(b)**2-r**2))