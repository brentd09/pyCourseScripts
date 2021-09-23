#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

# An example of unpacking args. See LP, p449

def unpackingArgs(a, b, c, d, e=1):
	print (a, b, c, d)
	
# This is a simple example

unpackingArgs(1, 2, 3, 4)

# this one unpacks a list to fill the positional params

args = [1, 2]
args += [3, 4]
unpackingArgs(*args)

# this one uses a dictionary.
# the keys here must match the parameters

args = { 'a': 10, 'b': 2, 'd': 4, 'c': 3 }
unpackingArgs(**args)

# some weird combos that also work. Ouch!

unpackingArgs(*(1, 2), **{'d': 4, 'c': 3})
unpackingArgs(1, *(2, 3), **{'d': 4})
unpackingArgs(1, c=3, *(2,), **{'d': 4})
unpackingArgs(1, c=3, *(2, 4)) # fails
unpackingArgs(1, *(2,), c=3, **{'d':4})


