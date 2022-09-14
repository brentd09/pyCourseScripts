fruits = ['   BANANA  ','OraNge     ',' PEar ']
cleanfruits = (fruit.strip().lower() for fruit in fruits)
print(list(cleanfruits))