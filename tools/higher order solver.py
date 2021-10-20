class matrix():
	def __init__(self,matrix=None,size=[]):
		if matrix!=None:
			self.m=matrix
		else:
			if len(size)!=2:
				Exception("must have exactly one row and one column")
			self.m=[[0 for i in range(size[0])] for i in range(size[1])]

	def __getitem__(self,item):
		return self.m[item]
	def __repr__(self):
		return "\n".join([
		" ".join([str(j) for j in i]) 
		for i in self.m])
	def col(self):
		return len(self.m)
	def row(self):
		return len(self.m[0])
	def __add__(self,other):
		if self.col()!=other.col() or self.row()!= other.row():
			raise Exception("for addition both must be of same row and column")
			return
		new=matrix(size=[self.row(),self.col()])
		for i in range(self.row()):
			for j in range(self.col()):
				new[j][i]=self.m[j][i]+other.m[j][i]
		return new
	def __sub__(self,other):
		other=matrix(matrix=[[j*-1 for j in i]for i in other])
		return (self+other)
	def __mul__(self,other):
		if self.row()!= other.col():
			Exception("cannot multiply")
		new=matrix(size=[self.col(),other.row()])
		for row in range(self.col()):
			for col in range(other.row()):
				for count in range(self.row()):
					new[row][col]+=self[row][count]*other[count][col]
		return new
	def __div__(self,other):
		return self/other
		#idk how do pls help
if __name__=="__main__":
	a=matrix([[100,100,100]])
	b=matrix([[200],[200],[200]])
	print(a*b)
	print(a+a)
	print(a-a)
