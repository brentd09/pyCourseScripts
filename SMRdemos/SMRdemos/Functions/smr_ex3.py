def outer1(a, b):
	def inner1():
		return a + b
		
	return inner1

def outer2():
	def inner2(a,b):
		return a + b
		
	return inner2
	
	
f = outer1(1,2)
g = outer2()

print (f())
print (g(1,2))
