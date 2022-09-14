#!/usr/bin/env python3

# changed to show class methods

class Auto:
    """This is the Auto class file"""
    howmany = 0 
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Auto.howmany += 1
    def __del__(self):
        Auto.howmany -= 1
        print("deleting: " + self.make)
        print("count is now:", Auto.howmany)

    @classmethod
    def count(cls):		# no self
        return cls.howmany
