from abc import ABCMeta, abstractmethod

class A(metaclass=ABCMeta):
    @abstractmethod
    def foo(self): pass

    @property           # must come first
    @abstractmethod
    def bar(self):
        pass

#A()  # raises TypeError

class B(A):
    def foo(self): print(42)

#B()  # raises TypeError

class C(A):
    def foo(self): print(42)

    @property               # gotcha
    def bar(self): return 42

c = C()         # works
c.foo()
print(c.bar)