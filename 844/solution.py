from math import isqrt

a, b = map(int, open("input.txt").read().split())
area = a * b
side = isqrt(area)
open("output.txt", "w").write(str(side if side * side == area else 0))
