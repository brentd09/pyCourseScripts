#!/usr/bin/env python3
import pickle

a_list = [10, 11, 12, 13]
a_tuple = ("A", "B", "C", "D")
a_set = {1, 2, 3, 4, 5, 6}
a_map = {'a':5,'b':6,'c':7}

# note: duplicate element

elements = [a_list, a_tuple, a_set, a_map, a_list]
f = open("output", "wb")

pickle.dump(elements, f)
f.close()
