with open("input.txt") as f:
    data = f.read().split()

n = int(data[0]) if data else 0
ones = sum(1 for x in data[1:1 + n * n] if x == "1")

with open("output.txt", "w") as f:
    f.write(f"{ones // 2}\n")
