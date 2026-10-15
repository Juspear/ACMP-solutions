with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
size = n * n
grid = [data[1 + i * size:1 + (i + 1) * size] for i in range(size)]
full = set(range(1, size + 1))

groups = []
for i in range(size):
    groups.append(grid[i])
    groups.append([grid[r][i] for r in range(size)])
for bi in range(n):
    for bj in range(n):
        groups.append([grid[bi * n + r][bj * n + c] for r in range(n) for c in range(n)])

correct = all(set(g) == full for g in groups)

with open('output.txt', 'w') as f:
    f.write('Correct\n' if correct else 'Incorrect\n')
