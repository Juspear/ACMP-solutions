with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
perm = data[1:n + 1]

inverse = [0] * n
for i, p in enumerate(perm):
    inverse[p - 1] = i + 1

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, inverse)) + '\n')
