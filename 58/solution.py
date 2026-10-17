with open("input.txt") as f:
    data = f.read().split()

pos = 0
t = int(data[pos])
pos += 1
answers = []

for _ in range(t):
    n, m = int(data[pos]), int(data[pos + 1])
    pos += 2
    grid = []
    for i in range(n):
        grid.append(data[pos:pos + m])
        pos += m
    nice = True
    for i in range(n - 1):
        for j in range(m - 1):
            if grid[i][j] == grid[i][j + 1] == grid[i + 1][j] == grid[i + 1][j + 1]:
                nice = False
                break
        if not nice:
            break
    answers.append("YES" if nice else "NO")

with open("output.txt", "w") as f:
    f.write("\n".join(answers) + "\n")
