m, n, i, j, c = map(int, open('input.txt').read().split())
if m * n % 2 == 0:
    ans = 'equal'
else:
    corner = c if (i + j) % 2 == 0 else 1 - c
    ans = 'black' if corner == 0 else 'white'
open('output.txt', 'w').write(ans)
