#!/usr/bin/env python

# simple function decorator example; LP pp 990ff

def trace(F):
	def wrapper(*args):
		print ("... calling", F.__name__)
		return F(*args)
		
	return wrapper

@trace
def aMethod(a, b):
	print (a+b)
aMethod(1, 2)	# effectively wrapper(aMethod)(1,2)
	
@trace
def bMethod(a, b):
	print (a+b)
	
bMethod("cat", "dog")
