class parallilogrammo:
	def __init__(self,x1,y1,x2,y2):
		self.x1=x1
		self.y1=y1
		self.x2=x2
		self.y2=y2

	def embadon(self):
		emb=(abs(self.y1-self.y2))*(abs(self.x1-self.x2))
		return emb

	def simeio(self,x,y):
		if (self.x1<=x and x<=self.x2) and (y<=self.y1 and self.y2<=y):
			return True
		else:
			return False

p1=parallilogrammo(1,5,8,1)
p2=parallilogrammo(2,6,9,2)
print(p1.embadon())
print(p2.simeio(5,5))

