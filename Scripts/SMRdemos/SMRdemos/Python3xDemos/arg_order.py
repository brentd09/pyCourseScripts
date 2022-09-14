def products1(begin, *items):
    res = begin
    for i in items:
        res *= i
    return res

n = products1(2, 3, 4)

def product2(*items, begin = 1):
    res = begin
    for i in items:
        res *= i
    return res

n = product2(2, 3, begin=10)

pass