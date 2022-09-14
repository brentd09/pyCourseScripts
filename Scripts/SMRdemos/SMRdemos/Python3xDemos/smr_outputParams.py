#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

# An example of simulating output params. See LP, p441

def minmax(*args):
	lo = min(args)
	hi = max(args)
	return (lo, hi)

a, b = minmax(1, 2, 8, -7, 4, 99)
print (a,b)
