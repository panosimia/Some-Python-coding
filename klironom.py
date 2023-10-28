import math
class Shape():
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def epistrofh(self):
		return (self.x,self.y)

class circle(Shape):
	def __init__(self,x,y,r):
		Shape.__init__(self,x,y)
		self.r=r
	def embadon(self):
		return math.pi*self.r**2

	def perifereia(self):
		return 2*math.pi*self.r

class square(Shape):
	def __init__(self,x,y,s):	
		Shape.__init__(self,x,y)
		self.s=s	
	def embadon2(self):
		return self.s**2

	def perifereia2(self):
		return 2*self.s


p1=Shape(2,3)
print('Shmeio:',p1.epistrofh())
p2=circle(2,3,4)
print('Embadon Kyklou:',p2.embadon())
print('Perifereia Kyklou:',p2.perifereia())
p3=square(2,3,5)
print('Embadon Tetragwnou:',p3.embadon2())
print('Perifereia Tetragwnou:',p3.perifereia2())
