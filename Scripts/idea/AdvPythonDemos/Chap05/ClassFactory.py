def createclass(name, bases, dict):
    return type(name, bases, dict)


c1 = createclass("C1", (object,), {"a": 42})
print(c1)

o1 = c1()
print(o1)
print(type(o1))
print(o1.a)

#

def createinstance(name, bases, dict):
    return type(name, bases, dict)()  # note ctor call


o2 = createinstance("C2", (object,), {"x": 0, "y": 1})
print(o2)
print(type(o2))
print(o2.y)
