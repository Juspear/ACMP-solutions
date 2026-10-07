with open("input.txt") as f:
    data = f.read().split()

k = int(data[0])
result = []
for i in range(k):
    n = int(data[1 + 2 * i])
    m = int(data[2 + 2 * i])
    result.append(19 * m + (n + 239) * (n + 366) // 2)

with open("output.txt", "w") as f:
    f.write("\n".join(map(str, result)) + "\n")
