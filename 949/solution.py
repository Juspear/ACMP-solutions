n, a, b = map(int, open('input.txt').read().split())
for _ in range(n - 1):
    a, b = b - a, a
open('output.txt', 'w').write(f'{a} {b}')
