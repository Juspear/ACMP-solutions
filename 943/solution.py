n, m, y, x = map(int, open('input.txt').read().split())
start = (y - 1) * m
if y % 2 == 1:
    ans = start + x - 1
else:
    ans = start + m - x
open('output.txt', 'w').write(str(ans))
