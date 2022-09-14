#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

# An example of keyword only args. Python 3+.
# The "*" prevents positional parameters from being used.

def keywordOnlyArgs(*, a = 1, b = 2):
	print (a, b)
	
keywordOnlyArgs(a = 3)
keywordOnlyArgs(b = 4)
keywordOnlyArgs(b = 4, a = 3)
keywordOnlyArgs(3, 4)
