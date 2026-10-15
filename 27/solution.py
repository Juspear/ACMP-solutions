with open('input.txt') as f:
    data = list(map(int, f.read().split()))

w, h, n = data[0], data[1], data[2]
diff = [[0] * (w + 1) for _ in range(h + 1)]
for i in range(n):
    x1, y1, x2, y2 = data[3 + 4 * i:7 + 4 * i]
    diff[y1][x1] += 1
    diff[y1][x2] -= 1
    diff[y2][x1] -= 1
    diff[y2][x2] += 1

for y in range(h + 1):
    for x in range(1, w + 1):
        diff[y][x] += diff[y][x - 1]
for y in range(1, h + 1):
    for x in range(w + 1):
        diff[y][x] += diff[y - 1][x]

white = sum(1 for y in range(h) for x in range(w) if diff[y][x] == 0)

with open('output.txt', 'w') as f:
    f.write(str(white) + '\n')
