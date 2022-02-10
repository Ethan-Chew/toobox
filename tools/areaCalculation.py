import math

def triangle(base, height):
    return 1/2 * base * height

def sine_rule_side(a,A,b): # Sine Rule (Sides) want to find side B
    return math.sin(b)*(A/math.sin(a))

def sine_rule_angle(a,A,B): # Sine Rule (Angles) want to find angle b
    return math.asin(B*(math.sin(a)/A))
def cosine_rule_angle(C,A,B):
     # Cosine Rule (Angles) find angle c
    return math.acos(((A**2+B**2-C**2)/(2*A*B)))
def cos_rule_side(c,A,B): # Cosine Rule (Sides) find side c
    return math.sqrt(A**2+B**2-(math.cos(c)*2*A*B))
    
def solve_triangle(A,B,C,a,b,c):
    # capital letters are sides, lowercase are angles
    if ((A!="?")+(B!="?")+(C!="?")+(a!="?")+(b!="?")+(c!="?"))<3:
        return "Triangle not possible"
    # Everything in radians btw, cuz math uses radians
    # If the value is "?" then is unknown
    if ((A!="?")+(B!="?")+(C!="?")) == 3:
        # know all sides
        c=cosine_rule_angle(C,A,B)
        b=sine_rule_angle(c,C,B)
        a=sine_rule_angle(c,C,A)
        area=1/2*A*B*math.sin(c)
        return [A,B,C,a,b,c,area]
    elif ((A!="?")+(B!="?")+(C!="?")) == 2:
        #lazy so reshuffle
        if A=="?":
            A=C
            d=c
            c=a
            a=d
        elif B=="?":
            B=C
            d=c
            c=b
            b=d
        # A, B is known, C is not known
        if c!="?":
            area=1/2*A*B*math.sin(c)
            C=cos_rule_side(c,A,B)
            b=sine_rule_angle(c,C,B)
            a=sine_rule_angle(c,C,A)
            return [A,B,C,a,b,c,area]
        else:
            if b=="?":
                b=sine_rule_angle(a,A,B)
                c=(math.pi-a)-(b)

                return solve_triangle(A,B,C,a,b,c)
            else:
                c=(math.pi-b)-(math.asin(A*(math.sin(b)/B)))
                return solve_triangle(A,B,C,a,b,c)
    else:
        # There are at least 2 angles
        # Lets make find all the angles
        if a=="?":
            a=(math.pi-b)-c
        elif b=="?":
            b=(math.pi-a)-c
        else:
            c=(math.pi-b)-a
        # Now all angles are known
        if A=="?" and B=="?" and C=="?":
            return "Not possible, there are multiple triangles"
        else:
            #solve using SAS
            #i mean solve all sides
            if A!="?":
                B=sine_rule_side(a,A,b)
                C=sine_rule_side(a,A,c)
            elif B!="?":
                A=sine_rule_side(b,B,a)
                C=sine_rule_side(b,B,c)

            else:
                A=sine_rule_side(c,C,a)
                B=sine_rule_side(c,C,b)

            #now we know all
            area=1/2*A*B*math.sin(c)
            return [A,B,C,a,b,c,area]
            

def parallelogram(base, slantHeight):
    return float(base) * float(slantHeight)

def trapezium(topBase, bottomBase, height):
    return ((float(topBase) + float(bottomBase))/2.0) * float(height)

def circle(radius):
    return float(math.pi * float(float(radius)**2))

def sector(radius, angle):
    return (math.pi * float(float(radius) ** 2)*(float(angle)/(2*180)))
if __name__=="__main__":
    therightans=[3,3,3,math.pi/3,math.pi/3,math.pi/3]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                temp=list(therightans)
                for l in range(len(temp)):
                    if l==i or l==j or l==k:
                        pass
                    else:
                        temp[l]="?"
                ans=solve_triangle(*temp)
                if type(ans)!=str:
                    print(ans,therightans)
                    for i in range(len(ans)-1):
                        if abs(ans[i]-therightans[i] )>0.00001:
                            print(ans)
                            print(therightans)
                            print(i)
                            print(ans[i])
                            print(therightans[i])
                            print(ans[i]-therightans[i])
                            print("\n")
                if type(ans[6])==float:
                    if ans[6]>=4.1:
                        exit()
                else:
                    pass
                    
