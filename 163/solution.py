with open("input.txt") as f:
    s = f.read().strip()

a, op, b, c = s[0], s[1], s[2], s[4]
sign = 1 if op == "+" else -1

if a == "x":
    x = int(c) - sign * int(b)
elif b == "x":
    x = sign * (int(c) - int(a))
else:
    x = int(a) + sign * int(b)

with open("output.txt", "w") as f:
    f.write(str(x))
