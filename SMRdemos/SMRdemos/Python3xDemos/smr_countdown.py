# demonstrate a coroutine

def countdown(count):
    while count > 0:
	    yield count
	    count -= 1  
    yield "Thunderbirds are go!"  

for n in countdown(5):
	print(n)
