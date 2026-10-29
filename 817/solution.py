n, m, d, k = map(int, open('input.txt').read().split())
open('output.txt', 'w').write(str((n + m) * d * k - n * m * d * d))
