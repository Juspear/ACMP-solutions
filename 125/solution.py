with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n = data[0]
matrix = [data[1 + i * n:1 + (i + 1) * n] for i in range(n)]
colors = data[1 + n * n:1 + n * n + n]

bad = 0
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] and colors[i] != colors[j]:
            bad += 1

with open('output.txt', 'w') as f:
    f.write(str(bad) + '\n')
