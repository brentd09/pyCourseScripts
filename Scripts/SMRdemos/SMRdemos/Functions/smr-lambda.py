#!/usr/bin/env python

# This is a not-quite simple example of using a lambda
# It's not a great example, since f is not anonymous
# Note the use of a variable outside of the lambda

f = lambda x : x * y

y = 1
print (f(8))
y = 2
print (f(8))
print ()

# the real power of lambdas comes with anonymous functions, usually as
# parameters to other functions such as map() and filter()

data = [ 1, 7, 2, 99, 20, 42]
for square in map(lambda x : x * x, data): print (square)
print ()
for where in filter(lambda x : x > 10, data): print (where)
