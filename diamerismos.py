def f(x):
	return x**2+2*x+1
Q=[]
L=[]
a=0
b=1
n=2
d=(b-a)/n
for i in range(n+1):
	L.append(a+i*d)
	Q.append(f(a+i*d))
print(L)
print(Q)

	
