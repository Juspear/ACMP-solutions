with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
grid = data[1:1 + n]
total = sum(row.count("C") for row in grid)

order = []
for i in range(n):
    cols = range(n) if i % 2 == 0 else range(n - 1, -1, -1)
    for j in cols:
        order.append((i, j))

result = [[2] * n for _ in range(n)]
cities = 0
for i, j in order:
    if cities == total // 2:
        break
    result[i][j] = 1
    if grid[i][j] == "C":
        cities += 1

with open("output.txt", "w") as f:
    f.write("\n".join("".join(map(str, row)) for row in result) + "\n")
