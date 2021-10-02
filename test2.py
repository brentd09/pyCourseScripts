import re
def add_dots(data):
  return ".".join(data)

def remove_dots(data):
  return re.sub("\.","",data)


print(add_dots("thisiscool"))