with open("input.txt") as f:
    data = f.read().split()

n = int(data[0])
count = [0] * 201
for token in data[1:n + 1]:
    count[int(token) + 100] += 1

parts = []
for value in range(201):
    if count[value]:
        parts.append((str(value - 100) + " ") * count[value])

with open("output.txt", "w") as f:
    f.write("".join(parts).rstrip() + "\n")
