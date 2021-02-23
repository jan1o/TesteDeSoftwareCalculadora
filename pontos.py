import math
from math import sqrt

def distanciaPontosReta(x1, y1, x2, y2):
    dist = ((x2) - (x1))**2 + ((y2) - (y1))**2
    distAB = sqrt(dist)
    return distAB

def distanciaPontosEspaco(x1, y1, z1, x2, y2, z2):
    dist = ((x2) - (x1))**2 + ((y2) - (y1))**2 + ((z2) - (z1))**2
    distABC = sqrt(dist)
    return distABC

def dist(x0, y0, x1, y1):
    a = ((x1) - (x0))**2 + ((y1) - (y0))**2
    b = math.sqrt(a)
    return b

# (x1, y1) -> -1, -2
# (x2, y2) -> -3, -44
#r: 42.04759208325728


print(dist(-1, -2, -3, -44))

print(math.pow(5,2))


