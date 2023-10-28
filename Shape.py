import math
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def getXYLoc(self):
        return(self.x,self.y)
class Circle(Shape):
    def __init__(self,x,y,r):
        Shape.__init__(self,x,y)
        self.r=r
    def area(self):
        return math.pi*self.r**2
    def circumference(self):
        return 2*math.pi*self.r

class Square(Shape):
    def __init__(self,x,y,s):
        Shape.__init__(self,x,y)
        self.s=s
    def area(self):
        return self.s**2
    def circumference(self):
        return self.s*4

s1=Shape(1,1)
print('Shape', s1.getXYLoc())

s2=Circle(2,2,1)
print('Circle', s2.getXYLoc(), s2.r, s2.area())
              
s3=Square(5,-5,3)
print('Square', s3.getXYLoc(), s3.s, s3.area())

shapes=[s2,s3]
for s in shapes:
    print(s.area(), s.circumference())


    
        
    
