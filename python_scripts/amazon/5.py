class printme():
	def __init__(self,msg):
		self.msg = msg
		print("message saved here")
	
	def printmm(self):
		print("string entered",self.msg)
		print("upper case is",self.msg.upper())
message=input()

a=printme(message)


a.printmm()
