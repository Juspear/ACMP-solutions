with open("input.txt") as f:
    data = f.read().split()

n, m = int(data[0]), int(data[1])
field = data[2:2 + n]


def free(i, j):
    return not (0 <= i < n and 0 <= j < m) or field[i][j] == "."


count = 0
for i in range(n):
    for j in range(m):
        if field[i][j] == "." and free(i - 1, j) and free(i + 1, j) and free(i, j - 1) and free(i, j + 1):
            count += 1

with open("output.txt", "w") as f:
    f.write(str(count))
