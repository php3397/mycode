import random
print("do you want me to generate a pass for you?")

def passwordgen():
	num=random.randint(1,100)
	return(num)


ans=input()

if ans == "yes" or ans == "Yes":
	newpassword=passwordgen()
	print(newpassword) 


charss = ["!","@","#","$","%","^"]
def ispassword(pswd):
	for i in pswd:
		if i in charss:
			if i.isalpha or i.isdigit:
				print("password is good")



ispassword(input())	
