#Create a class named Person, with firstname and lastname properties, and a printname method:


class Person():
	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname
	def printname(self):
		print(self.firstname,"-",self.lastname)


ob1 = Person("Prashant","Pujar")
ob1.printname()
