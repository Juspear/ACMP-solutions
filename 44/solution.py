with open("input.txt") as f:
    s = f.read().strip()

count = 0
for i in range(len(s) - 4):
    if s[i:i + 5] in (">>-->", "<--<<"):
        count += 1

with open("output.txt", "w") as f:
    f.write(f"{count}\n")
