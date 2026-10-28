moves = open("input.txt").read().strip()
swaps = {"A": (1, 2), "B": (2, 3), "C": (1, 3)}
pos = 1
for m in moves:
    a, b = swaps[m]
    if pos == a:
        pos = b
    elif pos == b:
        pos = a
open("output.txt", "w").write(str(pos))
