x=input('Give a number: ')
x=float(x)
y=input('Give a number: ')
y=float(y)
z=input('Give a number: ')
z=float(z)
max= None
if x%2!=0:
    max=x
if y> max and y%2 !=0:
    max=y
if z> max and z%2 !=0:
    max=z
print('max=',max)
