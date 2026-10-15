with open("input.txt") as f:
    start, dur = f.read().split("\n", 1)

h, m = map(int, start.strip().split(":"))
dh, dm = map(int, dur.split())
total = (h * 60 + m + dh * 60 + dm) % (24 * 60)

with open("output.txt", "w") as f:
    f.write(f"{total // 60:02d}:{total % 60:02d}")
