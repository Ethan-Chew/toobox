tokens=['+','-','*','/',"(",")"]
def is_float(value):
  try:
    float(value)
    return True
  except:
    return False
class algebric:
    def __init__(self, coeff,var,power=1):
        self.coef=coeff
        self.var=var
        self.power=power
def solveineq(inp):
    ine=0
    if "<" in inp:
        inp=inp.split("<")
        ine=1
    else:
        inp=inp.split(">")
        ine=-1
    leftside=inp[0]
    rightside=inp[1]
    # parse expression

def parse(expression):
    parsed=[]
    temp=''
    for i in expression:
        if i in tokens:
            temp=temp.strip()
            if is_float(temp):
                temp=float(temp)
            elif is_float(temp[:-1]):
                temp=algebric(float(temp[:-1]),temp[-1])
            parsed.append(temp)
            temp=''
            parsed.append(i)
        else:
            temp+=i
    parsed.append(temp)
    return parsed

def findend(s,j):
    count=1
    for i in range(j+1,len(s)):
        if s[i]=="(":
            count+=1
        elif s[i]==")":
            count-=1
        if count==0:
            return i+1
def culculate(thing):
    culculationdone=False
    while culculationdone==True:
        culculationdone=False
        if "*" in thing or "/" in thing:
            temp=[]
            for i in range(len(thing)):
                if thing[i]=="*":
                    prev=temp[-1]
                    nex=thing[i+1]
                    ans=0
                    if type(prev)==algebric and type (nex)==algebric:
                        if prev.coef ==nex.coef:
                            ans=algebric(prev.coef*nex.coef,prev.var,prev.power+nex.power)
                        else:
                            ans=algebric(prev.coef*nex.coef,sorted(prev.var+nex.var),prev.power+nex.power)
                    temp[-1]=ans
                if thing[i]=="/":
                    prev=temp[-1]
                    nex=thing[i+1]
                    temp[-1]=divide(prev,nex)
                
            
                
# reduces everything to 3x+1
def reduce(pe):
    reduced=[]
    i=0
    val=''
    while i<len(pe):
        val=pe[i]
        if val=="(":
            end=findend(pe,i)
            print(pe[i+1:end-1])
            reduced+=reduce(pe[i+1:end-1])
            i=end
        else:
            reduced.append(val)
        i+=1
    reduced=culculate(reduced)
    return reduced
if __name__ == "__main__":
    print(reduce(parse("(x+2)*(x+1)")))
    print(type(algebric(10,"a"))==algebric)
#print(reduce(parse("10x+2-(3+4-(3-2))")))
        
            
