with open('input.txt') as f:
    n, m, k = map(int, f.read().split())

with open('output.txt', 'w') as f:
    f.write('YES' if n * m >= k else 'NO')
