#!/usr/bin/env python

import sys

limit = 101
if len(sys.argv) > 1:
    limit = int(sys.argv[1]) + 1

primes = [True] * limit

for num in range(2, limit):
    if primes[num]:
        print(num, end=' ')
        for multiple_of_num in range(2 * num, limit, num):
            primes[multiple_of_num] = False
