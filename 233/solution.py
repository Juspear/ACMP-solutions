with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
heights = list(map(int, data[1:n + 1]))

answer = "No crash"
for i, h in enumerate(heights, 1):
    if h <= 437:
        answer = f"Crash {i}"
        break

with open("output.txt", "w") as f:
    f.write(answer + "\n")
