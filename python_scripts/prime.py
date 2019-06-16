

status=0		
prime=[]
def listpal(num):
		for j in (2,num):
			if num != j:
				if num%j == 0:
					status=0
			if status == 1:
				prime.append(num)

listpal(5)
for k in prime:
	print(k)
