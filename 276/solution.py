with open("input.txt") as f:
    n, m = map(int, f.read().split())

q, r = divmod(n, m)
parts = [q] * (m - r) + [q + 1] * r

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, parts)))
