class test:
	def __init__(self,a,b):
		self.a=a
		self.b=b

	def add(self):
		print("inside")
		return self.a+self.b
	def sub(self):
		return self.a-self.b
	def multiply(self):
		return self.a*self.b
	def devide(self):
		if self.b!=0:
			return self.a/self.b

