#!/usr/bin/env python3
import pickle

f = open("output", "rb")
obj = pickle.load(f)
print(obj)

a_list = obj[0]
a_list[0] = 42

print (obj)

f.close()
