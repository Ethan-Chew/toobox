import re


class algebric:
	def __init__(self,number,algebric={}):
		if number==0 and (algebric):
			number=1
		self.num=number
		self.al=algebric
	def __repr__(self):
		return str(self.num)+' '.join([a+"^"+str(self.al[a]) for a in self.al])
	def ha(self):
		return bool(self.algebric)
class calculator:
	def is_float(self,value):
		try:
			float(value)
			return True
		except:
			return False
	def find_end_num(self,value):
		#find the end of the number
		
		number="F"
		for i in range(len(value),0,-1):
			if self.is_float(value[:i]):
				number=value[:i]
				end=i
				break
		if number=="F":
			return 0
		else:
			return number
	def __init__(self):
		self.tokens={"*":(lambda x,y: self.mul(x,y)) , "/":(lambda x,y: self.div(x,y)) , "+":(lambda x,y: self.add(x,y)) , "-":(lambda x,y: self.minus(x,y))  }
	def turn(self, strin):
		# turns something like 1abc to a algebric type
		
		number=0.0
		algebras={}
		end=0
		for i in range(len(strin),-1,-1):
			if self.is_float(strin[:i]):
				number=float(strin[:i])
				end=i
				break
		strin=strin[i:]
		i=0
		while i<len(strin):
			if strin[i] =="^":
				n=self.find_end_num(strin[i+1:])
				algebras[strin[i-1]]=float(n)
				i+=len(n)
			else:
				algebras[strin[i]]=1
			i+=1

		return algebric(number,algebras)

	def findend(self,s,j):
		count=1
		for i in range(j+1,len(s)):
			if s[i]=="(":
				count+=1
			elif s[i]==")":
				count-=1
			if count==0:
				return i+1

	def sol(self,stri):
		parsed=self.parse(stri)
		return self.solve(parsed)

	def parse(self,stri):
		#parseing the eqation
		parsed=[]
		buf=''
		i=0
		while i<len(stri):
			if stri[i]=="(":
				end=self.findend(stri,i)
				if len(buf)>0:
					parsed.append(self.turn(buf))
					parsed.append("*")
					buf=""
				parsed.append(self.parse(stri[i+1:end-1]))
				
				i=end-1
			elif stri[i] in self.tokens:
				if len(parsed)>0 and type(parsed[-1])==list:
					parsed.append("*")
				if len(buf)>0:
					parsed.append(self.turn(buf))
				parsed.append(stri[i])
				buf=""
			else:
				buf+=stri[i]
			
			i+=1
		if len(buf)>0:
			if len(parsed)>0 and type(parsed[-1])==list:
				parsed.append("*")
			parsed.append(self.turn(buf))
			
		reparsed=[]
		#deal with double paranthesis
		if list in parsed:
			reparsed=[]
			for i in range(len(parsed)):
				if i>0 and type(parsed[i]) is list and (not (parsed[i-1] in self.tokens)):
					reparsed.append("*")
					reparsed.append(parsed[i])
				else:
					parsed.append(parsed[i])
			parsed=reparsed
		reparsed=[]
		# turn negative numbers into 0-1
		
		if parsed[0] in self.tokens:
			parsed=[algebric(0,{})]+parsed
		
		skip=0
		for i in range(len(parsed)):
			if skip!=0:
				skip-=1
			elif (i+1<len(parsed)) and type(parsed[i])==str and type(parsed[i+1])==str:
				reparsed.append([algebric(0,{}),parsed[i+1],parsed[i+2]])
				skip=1
			else:
				reparsed.append(parsed[i])
		parsed=reparsed
		return parsed

	def solve(self,parsed):
		# reduce all the parenthesis
		if list in parsed:
			reparsed=[]
			for i in parsed:
				if type(i) is list:
					reparsed.append(self.solve(i))
				else:
					reparsed.append(i)
			parsed=reparsed
		
		#reduce the paranthesis to the simplest form
		for i in range(len(parsed)):
			if type(parsed[i]) == list:
				parsed[i]=self.solve(parsed[i])
		
		#follow order of operation
		final=[]
		l=[]
		for i in range(len(parsed)):
			if i>0 and parsed[i-1]=="-":
				l[-1]="+"
				l.append(self.mul(parsed[i],algebric(-1)))
			else:
				l.append(parsed[i])
		parsed=list(l)
		print(type(parsed[0]))
		for j in self.tokens:
			i=0
			reparsed=[]
			while i<len(parsed):
				cur=parsed[i]
				if cur==j:
					if len(reparsed)>0:
						reparsed=reparsed[:-1]
					print(reparsed)
					reparsed+=(
						self.tokens[j](
							parsed[i-1],
							parsed[i+1])
						)
					i+=1
				else:
					reparsed.append(cur)
				i+=1
			parsed=list(reparsed)

		if len(parsed)==1:
			parsed=parsed[0]
		return parsed
	def mul(self,prev,nex):
		
		return [algebric(prev.num*nex.num)]

	def div(self,prev,nex):
		return [algebric(prev.num/nex.num)]
	def add(self,prev,nex):
		return [algebric(prev.num+nex.num)]
	








if __name__="__main__":

	a=calculator()

	print(a.sol("1+3(4+5)"))




