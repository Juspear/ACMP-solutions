lines = [s.strip() for s in open('input.txt').read().split('\n')]
lines = [s for s in lines if s]
n, m = map(int, lines[0].split())
best = None
winner = ''
for i in range(n):
    name = lines[1 + 2 * i]
    total = sum(map(int, lines[2 + 2 * i].split()))
    if best is None or total < best:
        best = total
        winner = name
open('output.txt', 'w').write(winner)
