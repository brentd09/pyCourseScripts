#!/usr/bin/env python

import urllib.request

u = urllib.request.urlopen("https://www.python.org")

print(u.info())  # <1>
print()

bytes = u.read(500)
print(bytes.decode())   # <2>
