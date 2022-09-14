#!/usr/bin/env python
'''
Spam -- provides a tasty breakfast
'''

# separator for toast toppings
_TOPSEP = " and "


def eggs(how):
    '''cook some eggs in some style'''
    print("Cooking up some lovely {} eggs".format(how))


def toast(*toppings):
    '''cook some toast'''
    print("Toasting up some toast with ", _TOPSEP.join(toppings))

if __name__ == "__main__":
    eggs('scrambled')
    toast("vegemite")
