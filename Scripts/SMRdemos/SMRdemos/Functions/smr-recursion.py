#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

# Some examples of recursion. See LP, p467

def sum1(L):
	# print (L)
	if not L:
		return 0
	else:
		return L[0] + sum1(L[1:])
		
print (sum1([1, 2, 3, 4]))

# this works with strings too

def sum2(L):
	# print (L)
	return L[0] if len(L) == 1 else L[0] + sum2(L[1:])
	
print (sum2([1, 2, 3, 4]))
print (sum2(['s', 'p', 'a', 'm']))

# but could be done with a loop

def sum3(L):
	tot = 0
	for n in L:
		tot += n
	return tot
	
print (sum3([1, 2, 3, 4]))
	
# more realistic example of mixing recursion and loops

def sumtree(L):
	tot = 0
	for x in L: # For each item at this level
		if not isinstance(x, list):
			tot += x # Add numbers directly
		else:
			tot += sumtree(x) # Recur for sublists
	return tot
	

L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting
print(sumtree(L))
