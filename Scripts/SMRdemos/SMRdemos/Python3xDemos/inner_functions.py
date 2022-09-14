def outer(a,b):
    x = 10
    y = 20

    def inner():
        print (a,b,x,y)

    return inner

f1 = outer(1,2)
f1()
