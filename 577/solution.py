with open("input.txt") as f:
    n, m = map(int, f.read().split())

text = "".join(str(i * j) for i in range(1, n + 1) for j in range(1, m + 1))

with open("output.txt", "w") as f:
    f.write("\n".join(str(text.count(str(d))) for d in range(10)))
