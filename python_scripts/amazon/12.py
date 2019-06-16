s=[]
save=[]

for i in range(9,21):
	if i%2 == 0:
		s.append(str(i))
flag=0
even=[1,3,5,7]
for j in s:
	for k in str(j):
		if int(k) in even:
			print("int k:flag set",k)
			flag=1
	if flag == 0:
		save.append(j)

print(save)
