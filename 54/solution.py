with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
k = [data[2 + i * m:2 + (i + 1) * m] for i in range(n)]

lower = max(min(row) for row in k)
upper = min(max(k[i][j] for i in range(n)) for j in range(m))

with open('output.txt', 'w') as f:
    f.write(f'{lower} {upper}\n')
