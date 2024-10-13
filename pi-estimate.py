import math
x = 10
n = 100000000000
while x <= n:
  print(x, "|", (x*math.tan(2*math.pi/x)))
  x = x*2
