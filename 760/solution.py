with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, v, length = data[0], data[1], data[2]
stops = sum(data[4 + 2 * i] for i in range(n))
time = length / v * 60 + stops

with open("output.txt", "w") as f:
    f.write("%.2f\n" % time)
