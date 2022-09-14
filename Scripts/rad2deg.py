from math import pi

def conv2deg (rad):
  deg = rad * 180 / pi
  return(deg)

print("{:.1f}".format(conv2deg(20)))