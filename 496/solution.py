with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:n + 1]
best = max(a[i - 1] + a[i] + a[(i + 1) % n] for i in range(n))

with open("output.txt", "w") as f:
    f.write(str(best))
