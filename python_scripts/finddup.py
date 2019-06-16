l1=[1,3,2,3,5,55]
print(l1)
l1.sort()
print(l1)
dup=0
b1=[1,2]
for x in b1:
	if l1[x] == l1[x+1]:
		dup=1

if dup == 1:
	print("dupe found")
else:
	print("no dupe found")
