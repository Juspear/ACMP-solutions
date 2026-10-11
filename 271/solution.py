with open("input.txt") as f:
    n = int(f.read())

a, b, idx = 1, 1, 2
while b < n:
    a, b = b, a + b
    idx += 1

with open("output.txt", "w") as f:
    if b == n:
        f.write(f"1\n{idx}")
    else:
        f.write("0")
