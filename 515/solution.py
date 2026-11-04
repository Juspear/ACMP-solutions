from math import hypot

with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
points = [(0, 0)] + [(data[1 + 2 * i], data[2 + 2 * i]) for i in range(n)] + [(0, 0)]
distance = sum(hypot(x2 - x1, y2 - y1) for (x1, y1), (x2, y2) in zip(points, points[1:]))

with open("output.txt", "w") as f:
    f.write(f"{distance:.3f}\n")
