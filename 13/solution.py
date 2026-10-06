with open('input.txt') as f:
    a, b = f.read().split()

bulls = sum(1 for i in range(4) if a[i] == b[i])
common = len(set(a) & set(b))

with open('output.txt', 'w') as f:
    f.write(f'{bulls} {common - bulls}')
