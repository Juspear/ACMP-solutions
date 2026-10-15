from math import hypot

with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n, c, p = data[0], data[1], data[2]
xs = data[3:3 + 2 * n:2]
ys = data[4:4 + 2 * n:2]
nx, ny = data[3 + 2 * n], data[4 + 2 * n]

best = None
for i in range(n):
    xi, yi = xs[i], ys[i]
    total = hypot(xi - nx, yi - ny) + sum(map(hypot, [x - xi for x in xs], [y - yi for y in ys]))
    if best is None or total < best:
        best = total

if abs(best - round(best)) < 1e-6:
    enough = c * round(best) <= p
else:
    enough = c * best <= p

with open('output.txt', 'w') as f:
    f.write('YES\n' if enough else 'NO\n')
