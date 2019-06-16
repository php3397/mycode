#factorial of a num
#fact3=3*2*1
fact=1
cal=1
num=int(input())
if num == 0:
	print ("fact is ",fact)
else:
	while (num > 1):
		cal = num * cal
		num = num-1

print(cal)
