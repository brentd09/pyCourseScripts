def fib():
    f = 0
    s = 1

    def fibonnaci():
        nonlocal f
        nonlocal s

        next, f, s = f, s, f+s
        return next

    return fibonnaci

f = fib()
for i in range(10):
    print(f())