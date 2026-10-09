with open("input.txt") as f:
    n, i, j = map(int, f.read().split())

d = abs(i - j)

with open("output.txt", "w") as f:
    f.write(f"{min(d, n - d) - 1}\n")
