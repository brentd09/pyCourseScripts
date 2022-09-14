def outer1(a, b):
	return lambda : a + b

def outer2():
	return lambda a,b : a + b
	
f = outer1(1,2)
g = outer2()

print (f())
print (g(1,2))
