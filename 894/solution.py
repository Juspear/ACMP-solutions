from math import pi, sqrt

s, r1 = map(float, open("input.txt").read().split())
r2 = sqrt(max(0.0, r1 * r1 - s / pi))
open("output.txt", "w").write(f"{r2:.3f}")
