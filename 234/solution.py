with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m, k = data[0], data[1], data[2]
mine = [[False] * m for _ in range(n)]
for i in range(k):
    r, c = data[3 + 2 * i] - 1, data[4 + 2 * i] - 1
    mine[r][c] = True

lines = []
for i in range(n):
    row = []
    for j in range(m):
        if mine[i][j]:
            row.append("*")
            continue
        cnt = 0
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                a, b = i + di, j + dj
                if 0 <= a < n and 0 <= b < m and mine[a][b]:
                    cnt += 1
        row.append(str(cnt) if cnt else ".")
    lines.append("".join(row))

with open("output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
