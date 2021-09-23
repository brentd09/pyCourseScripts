# function decorators can be classes too
# but they don't work with methods


class CDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print("self:", type(self))
        print("len(args), args[0]:", len(args), type(args[0]))
        self.func(*args)          # doesn't work: self is CDecorator, not Demo, instance. We need d

class Demo:
    @CDecorator
    def method1(self, x, y):
        print("x, y:", x, y)


d = Demo()
d.method1(1, 2)
