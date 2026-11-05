data = list(map(int, open("input.txt").read().split()))
m, n = data[0], data[1]
a = set(data[2:2 + m])
b = set(data[2 + m:2 + m + n])
with open("output.txt", "w") as f:
    f.write("1" if a == b else "0")
