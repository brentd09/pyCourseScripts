#!/usr/bin/env python
L1 = [1, 2, 3]
L2 = [4, 5, 6]

a = [L1, L2]
b = list(a)

print (a)
print (b)
print ()

a[0] = [7,8,9]

print (a)
print (b)
print ()

a[1][0] = 10

print (a)
print (b)
print ()
