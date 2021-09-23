#!/usr/bin/env python

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def __getattr__(self, name):
		print ("getting", name)
		return self.__dict__[name]
		
	def __setattr__(self, name, value):
		print ("setting", name)
		self.__dict__[name] = value
		
p = Person("Steve", 40)
p.age += 1
print (p.age)

p.age = p.age + 1
print (p.age)

# getter only called for undefined attributes
# can use __getattribute__ for all, BUT be careful :-)

# print (p.address)
