with open("input.txt") as f:
    a1, a2, n = map(int, f.read().split())

with open("output.txt", "w") as f:
    f.write(str(a1 + (n - 1) * (a2 - a1)))
