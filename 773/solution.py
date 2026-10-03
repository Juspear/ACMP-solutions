with open('input.txt') as f:
    k, m = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write(str(k * k * m))
