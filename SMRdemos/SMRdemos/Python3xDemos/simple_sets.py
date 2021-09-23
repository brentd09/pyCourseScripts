myset = { 'apple', 'pear', 'banana', 'apple', 'grape' }
print(len(myset))

myset = set("mississippi")
print(len(myset))

# can make a set from any sequence

aList = 'fe fi fo fum fi'.split()
myset = set(aList)
print(len(myset))