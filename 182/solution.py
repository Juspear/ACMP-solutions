with open('input.txt') as f:
    x1, y1, x2, y2, x3, y3 = map(int, f.read().split())

points = [(x1, y1), (x2, y2), (x3, y3)]
for k in range(3):
    c = points[k]
    a, b = points[(k + 1) % 3], points[(k + 2) % 3]
    if (a[0] - c[0]) * (b[0] - c[0]) + (a[1] - c[1]) * (b[1] - c[1]) == 0:
        x, y = a[0] + b[0] - c[0], a[1] + b[1] - c[1]
        break

with open('output.txt', 'w') as f:
    f.write(f'{x} {y}\n')
