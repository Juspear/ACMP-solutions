with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
lo, hi = 1, 31
for i in range(n):
    a, b = data[1 + 2 * i], data[2 + 2 * i]
    lo = max(lo, a)
    hi = min(hi, b)

with open("output.txt", "w") as f:
    f.write("YES\n" if lo <= hi else "NO\n")
