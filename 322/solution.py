with open("input.txt") as f:
    s = f.read().strip()

res = []
a, b = 1, 2
while a <= len(s):
    res.append(s[a - 1])
    a, b = b, a + b

with open("output.txt", "w") as f:
    f.write("".join(res))
