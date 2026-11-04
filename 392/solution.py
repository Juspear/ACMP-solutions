with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
p = data[1:n + 1]
start = p.index("1")

with open("output.txt", "w") as f:
    f.write(" ".join(p[start:] + p[:start]) + "\n")
