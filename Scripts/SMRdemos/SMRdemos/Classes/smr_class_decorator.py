#!/usr/bin/env python

# simple class decorator example; LP pp 990ff


 
def intercept(C):
	class Wrapper:
		def __init__(self, *args):	 # On instance creation
			print ("... Wrapper.__init__")
			self.wrapped = C(*args)
		def __getattr__(self, name): # On attribute fetch
			print ("... Wrapper.__getattr__", name)
			return getattr(self.wrapped, name)
			
	return Wrapper

@intercept
class Example:
	def __init__(self, x, y):
		self.attr = "spam"

x = Example(1, 2)		# calls Wrapper(1,2)
print (x.attr)	# calls Wrapper.__getattr__(x, "attr")

#x.attr = "eggs"
print (x.attr)	# interesting ... think about it
