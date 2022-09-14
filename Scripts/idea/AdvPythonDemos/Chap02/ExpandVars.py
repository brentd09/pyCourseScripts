import os

messages = ("Your PATH is $PATH", "Your PATH is ${PATH}", "Your PATH is %PATH%")

for msg in messages:
    print(os.path.expandvars(msg))
