l1=[0,0,2,3,4,5]
n1=[]
x=1
for i in range(1,len(l1)-1):
	sum=l1[i]+l1[i+1]
	if sum > x:
		n1.append(l1[i])
print(n1)
l2=[]
l3=[]

for i in range(10,20):
	l2.append(i)

for i in l2:
	n=str(i)
	print(n[0],n[1])
	if n[0] == n[1]:
		l3.append(i)
	else:
		print("notequal")
print(l3)
