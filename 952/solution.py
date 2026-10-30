n, m = map(int, open('input.txt').read().split())
if n == 0 and m > 0:
    ans = 'Impossible'
else:
    lo = max(n, m)
    hi = n + m - 1 if m > 0 else n
    ans = f'{lo} {hi}'
open('output.txt', 'w').write(ans)
