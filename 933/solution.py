a, b, c, t = map(int, open("input.txt").read().split())
if t <= a:
    cost = t * b
else:
    cost = a * b + (t - a) * c
open("output.txt", "w").write(str(cost))
