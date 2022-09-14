def singleton(C):
    instance = None

    def onCall(*args):
        nonlocal instance
        if instance is None:
            instance = C(*args)
        return instance

    return onCall


@singleton
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


bob = Person('bob', 40000)  # Really calls OnCall
sue = Person('sue', 50000)

print(bob.name, sue.name)
