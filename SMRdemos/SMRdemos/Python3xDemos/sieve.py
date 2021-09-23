import math

limit = 201

nonPrime = set()

print("Primes less than", limit-1)

print(2, end=' ')
for n in range(3, limit, 2):
    if n not in nonPrime:
        print (n, end=' ')
        #for k in range(2*n, limit, n):
        #    nonPrime.add(k)
        nonPrime |= set(range(n, limit, n))

print()
