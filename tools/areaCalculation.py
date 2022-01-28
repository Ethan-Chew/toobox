import math

def triangle(base, height):
    return 1/2 * base * height

def sine_rule_side(a,A,b):
    return math.sin(b)*(A/math.sin(a))
def sine_rule_angle(a,A,B):
    return math.asin(B*(math.sin(a)/A))
def solve_triangle(A,B,C,a,b,c):
    if ((A!="?")+(B!="?")+(C!="?")+(a!="?")+(b!="?")+(c!="?"))<3:
        return "not possible"
    #everything in radians btw, cuz math uses radians
    # if the value is "?" then is unknown
    if ((A!="?")+(B!="?")+(C!="?")) == 3:
        s=(A+B+C)/2
        Area=math.sqrt(s*(s-A)*(s-B)*(s-C))
        return Area
    elif ((A!="?")+(B!="?")+(C!="?")) == 2:
        if A=="?":
            #need to check if this is copied or refrenced
            A=C
            d=c
            c=a
            a=d
        elif B=="?":
            #same as previous comment
            B=C
            d=c
            c=b
            b=d
        # A, B is known, C is not known
        if c!="?":
            Area=1/2*A*B*math.sin(c)
            return Area
            #need figure out the rest of them(A,B,c) is known
        else:
            if b=="?":
                
                b=sine_rule_angle(a,A,B)
                c=(math.pi-a)-(b)
                return solve_triangle(A,B,C,a,b,c)
            else:
                c=(math.pi-b)-(math.asin(A*(math.sin(b)/B)))
                return solve_triangle(A,B,C,a,b,c)
    else:
        # there are at least 2 angles
        #lets make find all the angles
        if a=="?":

            a=(math.pi-b)-c
        elif b=="?":
            b=(math.pi-a)-c
        else:
            c=(math.pi-b)-a
        #now all angles are known
        if A=="?" and B=="?" and C=="?":
            return "not possible, there are multiple triangles"
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
            Area=1/2*A*B*math.sin(c)
            return Area
            

def parallelogram(base, slantHeight):
    return base * slantHeight

def trapezium(topBase, bottomBase, height):
    return ((topBase + bottomBase)/2) * height

def circle(radius):
    return math.pi * float(radius)**2

def sector(radius, angle):
    return math.pi * radius ** 2 *(angle/(2*math.pi))
if __name__=="__main__":
    print(solve_triangle(4,3,"?","?","?",(math.pi/2)))
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
                if type(ans)==float:
                    if ans>=4.1:
                        print(temp)
                        exit()
                    print(ans)
                else:
                    pass
                    
