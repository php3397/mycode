
class salary_struct:
	def __init__(self, name, s, raise):
		self.name=name
		self.s=s
		self.raise=raise

	def calculateraise(self):
		newsalary = self.s+self.raise
		return newsalary

ob1=salary_struct()
changed=ob1.calculateraise(prashant,75000,30000)
print(changed)

