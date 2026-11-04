with open("input.txt") as f:
    data = list(map(int, f.read().split()))

n, m = data[0], data[1]
logs = data[2:2 + n]
possible = max(logs) <= m <= sum(logs) - (n - 1)

with open("output.txt", "w") as f:
    f.write("yes\n" if possible else "no\n")
