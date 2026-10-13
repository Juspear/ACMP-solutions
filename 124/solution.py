with open('input.txt') as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
degree = [0] * (n + 1)
for i in range(m):
    a, b = data[2 + 2 * i], data[3 + 2 * i]
    degree[a] += 1
    degree[b] += 1

with open('output.txt', 'w') as f:
    f.write(' '.join(map(str, degree[1:])) + '\n')
