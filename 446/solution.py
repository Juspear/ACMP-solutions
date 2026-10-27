with open("input.txt") as f:
    data = f.read().split()

n, m = int(data[0]), int(data[1])
picture = data[2:2 + n]
board = data[2 + n:2 + n + n * m]
bits = {".": 0, "B": 1, "G": 2, "R": 4}

ok = True
for i in range(n):
    for j in range(m):
        need = bits[picture[i][j]]
        if need & int(board[i * m + j]) != need:
            ok = False

with open("output.txt", "w") as f:
    f.write("YES" if ok else "NO")
