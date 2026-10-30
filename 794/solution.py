n, m, k = map(int, open('input.txt').read().split())
white = min(k - 1, m)
red = m // k
open('output.txt', 'w').write(str(n * (white + red)))
