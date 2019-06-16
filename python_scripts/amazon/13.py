counter=0
ina=0
capital=0
digit=[1,2,3,4,5,6,7,8,9]
with open("test.txt","r+") as fh:
	for i in fh:
		line=i
		for j in line:
			if j.isdigit():
				ina+=1
			if j.isalpha() and j.isupper():
				capital+=0
				counter+=1

print(capital)
print(ina)
print(counter)
