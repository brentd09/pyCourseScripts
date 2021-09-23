# simple examples from 5.1.3

pairs = [(x, y) for x in range(5) for y in range(5)]
print(pairs)
print()

pairs = [(x, y) for x in range(5) for y in range(5) if x < y]
print(pairs)
print()

# Nested list comprehensions from 5.1.4

matrix = (
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
)

transpose = [[row[i] for row in matrix] for i in range(4)]
print(transpose)
print()
