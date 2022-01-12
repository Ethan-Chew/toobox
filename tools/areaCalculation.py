import math

def triangle(base, height):
    return 1/2 * base * height

def solve_triangle(A,B,C,a,b,c):
    if (A=="?"+B=="?"+C=="?"+a=="?"+b=="?"+c=="?")<3:
        return "not possible"
    #everything in radians btw, cuz math uses radians
    # if the value is "?" then is unknown
    if (A=="?"+B=="?"+C=="?") == 3:
        c=math.acos( ( a**2 + b**2﹣c**2 )/( 2*a*b ) )
        
    elif (A=="?"+B=="?"+C=="?") == 2:
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
            #need figure out the rest of them(A,B,c) is known
        else:
            if b=="?":
                c=(math.pi-a)-(math.asin(B*(math.sin(a)/A)))
                return solve_triangle(A,B,C,a,b,c)
            else:
                c=(math.pi-b)-(math.asin(A*(math.sin(b)/B)))
                return solve_triangle(A,B,C,a,b,c)
    else:
        
            

def parallelogram(base, height):
    return base * slantHeight

def trapezium(base, height):
    return ((topBase + bottomBase)/2) * height

def circle(radius):
    return math.pi * radius**2

def sector(radius, angle):
    return math.pi * radius ** 2 *(angle/(2*math.pi))
