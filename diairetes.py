num=("Give a number: ")
num=int(num)
k=[]
for i in range(1,num+1):
	if num % i==0:
		k.append(i)
print(k)


