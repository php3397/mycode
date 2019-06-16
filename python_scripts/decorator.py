#p(x)=a.x^2+b.x+c
def poly(x,a,b,c):
	def function():
		return str(a*x+b*x+c)
	return function()

a=10
b=10
c=10
x=input()
value=poly(x,a,b,c)
print(value)	
