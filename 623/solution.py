with open("input.txt") as f:
    n = int(f.read())

a, b = 0, 1
for _ in range((n + 1) % 60):
    a, b = b, (a + b) % 10

with open("output.txt", "w") as f:
    f.write(f"{a}\n")
