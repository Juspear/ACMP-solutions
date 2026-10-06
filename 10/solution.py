with open('input.txt') as f:
    a, b, c, d = map(int, f.read().split())

roots = []
for x in range(-100, 101):
    if a * x ** 3 + b * x ** 2 + c * x + d == 0:
        roots.append(str(x))

with open('output.txt', 'w') as f:
    f.write(' '.join(roots))
