with open("input.txt") as f:
    s = f.read().strip()

diff = 0
for i, c in enumerate(reversed(s)):
    if i % 2 == 0:
        diff += int(c)
    else:
        diff -= int(c)

with open("output.txt", "w") as f:
    f.write("YES" if diff % 11 == 0 else "NO")
