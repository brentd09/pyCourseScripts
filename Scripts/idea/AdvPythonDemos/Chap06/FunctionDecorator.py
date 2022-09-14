from functools import wraps

def trace(method):

    @wraps(method)
    def wrapper(*args, **kwargs):
        print("Before:", len(args))
        method(*args, **kwargs)          # note access to original method
        print("After")

    return wrapper


@trace
def example(n):
    ''' My example function '''
    print(n)

example(42)

print(example, example.__doc__)

# does it work for methods?

class Demo:
    @trace
    def method(self, a):
        print(a)


d = Demo()
d.method(42)