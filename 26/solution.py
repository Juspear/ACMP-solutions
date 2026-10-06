with open('input.txt') as f:
    x1, y1, r1, x2, y2, r2 = map(int, f.read().split())

dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

if (r1 - r2) ** 2 <= dist <= (r1 + r2) ** 2:
    answer = 'YES'
else:
    answer = 'NO'

with open('output.txt', 'w') as f:
    f.write(answer)
