import math
class circle_equation():
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
if __name__ == "__main__":
    ceqn=circle_equation()
    print(ceqn.to_standard_form(-2,-4,-4))
    print(ceqn.to_general_form(-1,-2, 9))