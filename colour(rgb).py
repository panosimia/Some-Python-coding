class rgb:
	def __init__(self,red,green,blue):
		self.red=red
		self.green=green
		self.blue=blue
	def brightness(self):
		highest=max(self.red,self.green,self.blue)
		lowest=min(self.red,self.green,self.blue)
		c=(1/2)*(highest+lowest)/255
		return c

white=rgb(255,255,255)
red=rgb(255,0,0)
purple=rgb(255,0,255)
print(purple.brightness())
print(white.brightness())
