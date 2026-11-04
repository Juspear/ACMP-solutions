with open("input.txt") as f:
    shots = [tuple(map(int, line.split())) for line in f if line.strip()]

hit = set()
for x, y in shots:
    for i in range(5):
        cx = 25 * i
        if (x - cx) ** 2 + y ** 2 <= 100:
            hit.add(i)

with open("output.txt", "w") as f:
    f.write(f"{len(hit)}\n")
