import math
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        return self.x*other.x+self.y*other.y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)
    def __str__(self):
        return "(%g,%g)" %(self.x,self.y)


u=Vector(1,1)
w=Vector(0,1)
v=Vector(2,3)
print("u=",u)
print("w=",w)
print("v=",v)
a=u+v
b=v-u
c=u*v
print("abs(u)=",abs(u))
print("a=v+u=",a)
print("b=v-u=",b)
print("c=u*v=",c)
print("a == w ?", a == w)            
