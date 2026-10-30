g = open('input.txt').read().split()
lines = [row for row in g]
lines += [''.join(g[r][c] for r in range(3)) for c in range(3)]
lines.append(g[0][0] + g[1][1] + g[2][2])
lines.append(g[0][2] + g[1][1] + g[2][0])
if 'XXX' in lines:
    ans = 'Win'
elif 'OOO' in lines:
    ans = 'Lose'
else:
    ans = 'Draw'
open('output.txt', 'w').write(ans)
