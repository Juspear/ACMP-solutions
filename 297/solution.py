circles = {"0": 1, "6": 1, "8": 2, "9": 1}

with open("input.txt") as f:
    s = f.read().strip()

total = sum(circles.get(c, 0) for c in s)

with open("output.txt", "w") as f:
    f.write(f"{total}\n")
