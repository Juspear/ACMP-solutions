with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
d = [data[1 + i * n:1 + (i + 1) * n] for i in range(n)]

best = float("inf")
for i in range(n):
    row_i = d[i]
    for j in range(i + 1, n):
        row_j = d[j]
        base = row_i[j]
        for k in range(j + 1, n):
            total = base + row_j[k] + row_i[k]
            if total < best:
                best = total

with open("output.txt", "w") as f:
    f.write(str(best) + "\n")
