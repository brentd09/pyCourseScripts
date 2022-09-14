def repeat_each(seq, n):
    for x in seq:
        for i in range(n):
            yield x


def repeat_all(seq, n):
    # naive implementation doesn't work, since iterator can only run once
    for i in range(n):
        yield from seq


def bracket(seq, down=None, up=None):
    for x in seq:
        if up:
            for i in range(-down, 0):
                yield x * 2 ** i
        if down:
            for i in range(up + 1):
                yield x * 2 ** i


s = (100,)
s = bracket(s, down=2, up=2)
s = repeat_each(s, 2)
s2 = repeat_all(s, 3)

for result in s2:
    print(result)
