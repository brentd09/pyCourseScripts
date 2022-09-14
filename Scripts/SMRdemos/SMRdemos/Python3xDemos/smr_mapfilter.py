#!/usr/bin/env python

string_data = [ '-1', '0', '1', '2']
ints = map(int, string_data)
doubled = map(lambda x: x * 2, ints)
positives = filter(lambda x: x > 0, doubled)

for n in positives:
	print (n)
