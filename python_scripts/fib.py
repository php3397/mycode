a=0
b=1
c=a+b
d=c+b
s=[]
for i in range(15):
	s.append(i)
print(s)	
fib=[0,1]
for j in range(14):
	a=fib[j]	
	b=fib[j+1]
	f1=a+b
	fib.append(f1)

print(fib)

