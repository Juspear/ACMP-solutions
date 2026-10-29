lines = [s.strip() for s in open('input.txt').read().split('\n')]
n, m = map(int, lines[0].split())
rows = [s for s in lines[1:] if s]
src = rows[:n]
neg = rows[n:2 * n]
bad = 0
for i in range(n):
    for j in range(m):
        if src[i][j] == neg[i][j]:
            bad += 1
open('output.txt', 'w').write(str(bad))
