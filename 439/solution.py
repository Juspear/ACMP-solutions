with open("input.txt") as f:
    n, p = map(int, f.read().split())

serial = p / 100
time = serial + (1 - serial) / n

with open("output.txt", "w") as f:
    f.write(f"{1 / time:.9f}")
