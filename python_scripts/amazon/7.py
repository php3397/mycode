x=4
y=6
row=[]
col=[]
#l1=[r1c1[],r2c2[],r3c3[]]
l1=[]
for j in (1,x):
	rowval=j
	row.append(j)
	for i in range(len(row)):
		colvalue=i
		col.append(i)
		place= rowval * colvalue
		l1.append(place)
print(l1)
print(row,col)
