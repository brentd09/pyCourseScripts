colours = "red green blue".split()
print(colours)
print(dir(colours))

print('-'*20)

it = iter(colours)

print(it)
print(dir(it))

try:
    while True:
        c = next(it)
        print(c)
except:
    print('done')
