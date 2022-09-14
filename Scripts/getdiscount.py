import sys

if len(sys.argv) != 3:
  sys.exit(1)

price = float(sys.argv[1])
discount = float(sys.argv[2])

result = price - (price / 100 * discount)

print("{:.2f}".format(result))