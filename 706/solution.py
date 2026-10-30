r, x, y = map(int, open('input.txt').read().split())
dist = abs(x) * r / (2 * r - y)
open('output.txt', 'w').write(f'{dist:.2f}')
