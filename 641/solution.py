s = open("input.txt").read().strip()
for _ in range(2):
    i = 0
    while i < len(s) - 1 and s[i] >= s[i + 1]:
        i += 1
    s = s[:i] + s[i + 1:]
s = s.lstrip("0") or "0"
with open("output.txt", "w") as f:
    f.write(s)
