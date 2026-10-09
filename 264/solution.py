with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
temps = list(map(int, data[1:n + 1]))

best = 0
run = 0
for t in temps:
    run = run + 1 if t > 0 else 0
    best = max(best, run)

with open("output.txt", "w") as f:
    f.write(f"{best}\n")
