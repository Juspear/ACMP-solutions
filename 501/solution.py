with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
rects = []
for i in range(n + 1):
    x1, y1, x2, y2 = data[1 + 4 * i:5 + 4 * i]
    rects.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

bx1, by1, bx2, by2 = rects[-1]
area = 0
for x1, y1, x2, y2 in rects[:-1]:
    w = min(x2, bx2) - max(x1, bx1)
    h = min(y2, by2) - max(y1, by1)
    if w > 0 and h > 0:
        area += w * h

with open("output.txt", "w") as f:
    f.write(str(area) + "\n")
