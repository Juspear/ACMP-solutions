with open("input.txt") as f:
    n = int(f.read().split()[0])


def to_base(x, b):
    digits = []
    while x:
        digits.append(x % b)
        x //= b
    return digits


bases = []
for b in range(2, 37):
    d = to_base(n, b)
    if d == d[::-1]:
        bases.append(b)

with open("output.txt", "w") as f:
    if not bases:
        f.write("none\n")
    else:
        f.write("unique\n" if len(bases) == 1 else "multiple\n")
        f.write(" ".join(map(str, bases)) + "\n")
