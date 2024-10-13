import math
x = 10
n = 1000
while x <= n:
  print(x, "|", (x*math.tan(2*math.pi/x)))
  x += 1
