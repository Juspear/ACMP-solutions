data = list(map(int, open("input.txt").read().split()))
n = data[0]
limits = data[1:1 + n]
k = data[1 + n]
presses = [0] * n
for key in data[2 + n:2 + n + k]:
    presses[key - 1] += 1
with open("output.txt", "w") as f:
    f.write("\n".join("yes" if presses[i] > limits[i] else "no" for i in range(n)))
