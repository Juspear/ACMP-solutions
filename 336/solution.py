with open("input.txt") as f:
    s = f.read().strip()

cur = lo = hi = 0
for c in s:
    cur += 1 if c == "1" else -1
    lo = min(lo, cur)
    hi = max(hi, cur)

with open("output.txt", "w") as f:
    f.write(str(hi - lo + 1))
