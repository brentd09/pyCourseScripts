from functools import partial, partialmethod
import operator


def simple_func(x, y):
    '''

    :param x:
    :param y:
    :return:

        '''
    print("x", x, "y", y)


# Use partial with one keyword arg
p = partial(simple_func, y=10)
p(20)  # this works

p = partial(simple_func, x=10)
#p(20)           # this doesn't work
p(y=20)


# do partials work with methods?

class Demo:
    '''

    '''
    def simple_func(self, x, y):
        '''
        This is a fantastic function.

        :param x: An *important* parameter
        :param y: Even **more** important
        :return: Nothing useful
        :rtype: None
        '''
        print("x", x, "y", y)


c = Demo()
p = partial(c.simple_func, 42)
p(96)  # yep


# what are partial methods then?

class Cell:
    def __init__(self):
        self.alive = False

    def set_state(self, state):
        ''' useless comment '''
        self.alive = state

    # add some partials to the class

    part1 = partial(set_state, state=True)
    part2 = partialmethod(set_state, state=True)


c = Cell()
print(c.alive)

# Cell.part1()  # doesn't work: no self
Cell.part1(c)   # but this fixes it.
c.part2()       # but this acts like a normal method

print(c.alive)

# what is this operator.itemgetter ??

data = [('Steve', 3), ('Mike', 2), ('Steve', 1), ('Lorna', 4)]
data.sort()
print(data)

# sort on first item (0) from each tuple

data = [('Steve', 3), ('Mike', 2), ('Steve', 1), ('Jean', 4)]
data.sort(key=operator.itemgetter(0))       # only use item 0
print(data)
