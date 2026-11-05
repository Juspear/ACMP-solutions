n, m = map(int, open("input.txt").read().split())
with open("output.txt", "w") as f:
    f.write(str(n + 1) if m >= 1 else "NO")
