with open("input.txt") as f:
    x1, y1, x2, y2, xa, ya = map(int, f.read().split())

if x1 == x2:
    xb, yb = 2 * x1 - xa, ya
else:
    xb, yb = xa, 2 * y1 - ya

with open("output.txt", "w") as f:
    f.write(f"{xb} {yb}\n")
