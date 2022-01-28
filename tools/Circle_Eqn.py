import math
class circle_equation():
    def to_standard_form(self, a, b, c):
        f=(lambda A:"+ "+str(A) if A>0 else "- "+str(A)[1:])
        A=a/2
        B=b/2
        r=math.sqrt(A**2+B**2-c)
        return "(x {})^2 + (y {}) = {}^2".format(f(A),f(B),r)
    def to_general_form(self, a, b, r):
        f=(lambda A:"+ "+str(A) if A>0 else "- "+str(A)[1:])
        r=math.sqrt(r)
        return "x^2 + y^2 {}x {}y {} = 0".format(f(a*2),f(b*2),f(a**2+b**2-r**2))
if __name__ == "__main__":
    ceqn=circle_equation()
    print(ceqn.to_standard_form(-2,-4,-4))
    print(ceqn.to_general_form(-1,-2, 9))