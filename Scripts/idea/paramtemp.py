import sys

degc = sys.argv[1]
floatdegc = float(degc)
f = ((9 * floatdegc) /5) + 32
strf = str(f)
print (degc + ' in Deg C is ' + strf + ' degrees in F')