with open("input.txt") as f:
    cell = f.read().strip()

x = ord(cell[0]) - ord("a")
y = int(cell[1]) - 1
moves = []
for dx, dy in ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)):
    nx, ny = x + dx, y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        moves.append(chr(ord("a") + nx) + str(ny + 1))

with open("output.txt", "w") as f:
    f.write("\n".join(sorted(moves)) + "\n")
