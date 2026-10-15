with open('input.txt') as f:
    tokens = f.read().split()

n, m = int(tokens[0]), int(tokens[1])
grid = tokens[2:2 + n]

rows = [i for i in range(n) if '*' in grid[i]]
cols = [j for j in range(m) if any(grid[i][j] == '*' for i in range(n))]

result = []
for i in range(n):
    line = ''
    for j in range(m):
        inside = rows and rows[0] <= i <= rows[-1] and cols[0] <= j <= cols[-1]
        line += '*' if inside else '.'
    result.append(line)

with open('output.txt', 'w') as f:
    f.write('\n'.join(result) + '\n')
