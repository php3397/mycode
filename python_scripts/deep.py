class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def display(self):
		print("name",self.name)
		print("age",self.age)

class student(person):
	def __init__(self,rollno,name,age,per):
		self.rollno=rollno
		person.__init__(self,name,age)
		self.per=per
	def display(self):
		print("rollno per",self.rollno,self.per)
		print(person.display(self))



s1=student(101,'Hema',21,75.50)
print("stuent details")
s1.display()
