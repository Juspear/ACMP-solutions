import math

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

diag = 1 / math.sqrt(2)
moves = {
    1: (0, 1),
    2: (diag, diag),
    3: (1, 0),
    4: (diag, -diag),
    5: (0, -1),
    6: (-diag, -diag),
    7: (-1, 0),
    8: (-diag, diag),
}

n = data[0]
x = y = 0.0
for i in range(n):
    direction, steps = data[1 + 2 * i], data[2 + 2 * i]
    dx, dy = moves[direction]
    x += dx * steps
    y += dy * steps

x = round(x, 3) + 0.0
y = round(y, 3) + 0.0

with open("output.txt", "w") as f:
    f.write(f"{x:.3f} {y:.3f}\n")
