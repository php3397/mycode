class teststring:
	def __init__(self,sample):
		self.sample = sample

	def isupper(self):
		if (self.sample.isupper()):
			print("String is upper")
		else:
			print("string is lower")

ob1= teststring("prashant")
ob2= teststring("PRASHANT")
ob1.isupper()
ob2.isupper()
