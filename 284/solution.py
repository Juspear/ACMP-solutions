with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
a = data[1:n + 1]
m = int(data[n + 1])
pos = n + 2
lines = []
for _ in range(m):
    i, j = int(data[pos]), int(data[pos + 1])
    pos += 2
    lines.append(" ".join(a[i - 1:j]))

with open("output.txt", "w") as f:
    f.write("\n".join(lines) + "\n")
