L1=[1,2,4,6,8]
L2=[0,1,2,6]

found = False

for x in L1:
	if x in L2:
		found = True
		break

if found == True:
	print("Yes")
else:
	print("No")


			

