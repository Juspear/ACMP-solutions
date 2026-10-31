with open("input.txt") as f:
    n, m, ph, l = map(int, f.read().split())

both = m + ph + l - n

with open("output.txt", "w") as f:
    f.write(f"{both} {m - both} {ph - both}\n")
