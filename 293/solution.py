with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n = data[0]
profits = data[1:n + 1]
rates = data[n + 1:2 * n + 1]

best = 0
for i in range(n):
    if profits[i] * rates[i] > profits[best] * rates[best]:
        best = i

with open("output.txt", "w") as f:
    f.write(str(best + 1))
