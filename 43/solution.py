with open("input.txt") as f:
    s = f.read().strip()

best = max(len(part) for part in s.split("1"))

with open("output.txt", "w") as f:
    f.write(f"{best}\n")
