with open("input.txt") as f:
    n = int(f.read())

ans = n * (n - 1) * (n - 2) if n >= 3 else 0

with open("output.txt", "w") as f:
    f.write(f"{ans}\n")
