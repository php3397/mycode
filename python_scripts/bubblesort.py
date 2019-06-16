val=[11,40,12,3]
iter=[0,1,2]
iter1=[0,1,2]

for i in iter:
	for i in iter1:
		big=val[i]
		if big < val[i+1]:
			print("")
		else:
			val[i]=val[i+1]
			val[i+1]=big
print(val)
