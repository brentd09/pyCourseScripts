from Chap06.timerdecorator import timer


@timer(label='[lc]', trace=True)
def listcomp(N):
    return [x * 2 for x in range(N)]


@timer(label='[map]')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))


for func in (listcomp, mapcall):
    print('')
    func(10000)
    func(100000)
    func(1000000)
    print('alltime = {}'.format(func.alltime))
