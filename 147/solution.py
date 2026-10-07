with open("input.txt") as f:
    n = int(f.read())

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

with open("output.txt", "w") as f:
    f.write(str(a) + "\n")
