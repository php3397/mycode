#Q = Square root of [(2 * C * D)/H]
import math
def calculate(D):
	C=50
	H=30
	return math.sqrt(round((2 * C * D/H)))

num=input()
for i in num.split(","):
	save=calculate(int(i))
	print(save)
