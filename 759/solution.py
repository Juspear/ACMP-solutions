with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
values = sorted(data[2:2 + n], reverse=True)
total = sum(v for v in values[:m] if v > 0)

with open("output.txt", "w") as f:
    f.write(str(total))
