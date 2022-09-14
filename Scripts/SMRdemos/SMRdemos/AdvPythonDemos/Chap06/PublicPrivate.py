# based on LP4, pp 1029


def accessControl(failIf, traceMe=False):
    def trace(*args):
        if traceMe: print('[' + ' '.join(map(str, args)) + ']')

    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)  # note: use __ to mangle name

            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':  # mangled name
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)

        return onInstance

    return onDecorator


def Private(*attributes):
    return accessControl(failIf=lambda attr: attr in attributes, traceMe=False)


def Public(*attributes):
    return accessControl(failIf=lambda attr: attr not in attributes)


#@Private('age')  # Person = Private('age')(Person)
@Public('name')     # Person = Public('name')(Person)
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age


x = Person1('bob', 42)
print(x.name)
x.name = "sue"
# print(x.age)
# x.age = 21
x.addattr = "abc"
print(x.addattr)
