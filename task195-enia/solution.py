with open('input.txt') as f:
    n, a, b = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write(str(n * a * b * 2))
