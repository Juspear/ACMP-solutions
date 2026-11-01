with open("input.txt") as f:
    n = int(f.read().split()[0])

parts = []
group = ""
length = 0
k = 0
while length < n:
    k += 1
    group += str(k)
    parts.append(group)
    length += len(group)

sequence = "".join(parts)

with open("output.txt", "w") as f:
    f.write(sequence[n - 1])
