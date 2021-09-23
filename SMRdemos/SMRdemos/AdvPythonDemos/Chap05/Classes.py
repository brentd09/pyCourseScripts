class MyClass(object):
    classVar = 42

    def __init__(self, x, y):
        self.x = x
        self.y = y
        MyClass.z = 96

    def method1(self):
        pass

    def method2(self):
        self.method1()


print(MyClass)
print(dir(MyClass))

# create an instance

mc = MyClass(1, 2)
print(mc, "__class__", mc.__class__)

# the following is interesting. Is z an instance attribute? What about classVar?

print("Instance:\n", dir(mc))

# let's look at what's inside the class object proper

print("Class:\n", dir(MyClass))
print()

# access the vars using the instance only

print("Before: x {}, y {}, z {}, classVar {}".format(mc.x, mc.y, mc.z, mc.classVar))

# now hide z

mc.z = 3        # really setattr(mc, 'z', 3)

print('After: x {}, y {}, z {}, MyClass.z {}'.format(mc.x, mc.y, mc.z, MyClass.z))
