#!/usr/bin/env python

data = [ '-1', '0', '1' ]
for n in filter(lambda x: x > 0, map(int, data)):
	print (n)
